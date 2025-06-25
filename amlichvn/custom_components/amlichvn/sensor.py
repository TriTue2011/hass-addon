import logging
import sqlite3
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import STATE_UNKNOWN
from .const import DOMAIN, DB_PATH

_LOGGER = logging.getLogger(__name__)


def ensure_events_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tendukien TEXT,
            loaisukien TEXT,
            ngayam REAL,
            thangam REAL,
            namam REAL,
            ngayduong REAL,
            thangduong REAL,
            namduong REAL,
            mota TEXT,
            laplai TEXT
        )
        """
    )
    conn.commit()
    conn.close()


async def async_setup_entry(hass, config_entry, async_add_entities):
    ensure_events_table()
    sensors = []
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, tendukien, loaisukien, ngayam, thangam, namam, "
            "ngayduong, thangduong, namduong, mota, laplai FROM events"
        )
        rows = cursor.fetchall()
        conn.close()
        for row in rows:
            sensors.append(AmLichEventSensor(row))
    except Exception as ex:
        _LOGGER.error(f"Khong the doc events.db: {ex}")
    async_add_entities(sensors, True)


def parse_float_or_none(val):
    try:
        if val is None or val == "":
            return None
        return float(val)
    except Exception:
        return None


def format_int_if_possible(val):
    if val is None:
        return ""
    if isinstance(val, float) and val.is_integer():
        return str(int(val))
    return str(val)


class AmLichEventSensor(SensorEntity):
    def __init__(self, row):
        self._id = row[0]
        self._tendukien = row[1]
        self._loaisukien = row[2]
        self._ngayam = parse_float_or_none(row[3])
        self._thangam = parse_float_or_none(row[4])
        self._namam = parse_float_or_none(row[5])
        self._ngayduong = parse_float_or_none(row[6])
        self._thangduong = parse_float_or_none(row[7])
        self._namduong = parse_float_or_none(row[8])
        self._mota = row[9]
        self._laplai = row[10]
        # Log chi tiet gia tri va kieu du lieu cac truong so
        _LOGGER.warning(
            f"[DEBUG amlichvn] id={self._id} tendukien={self._tendukien} "
            f"loaisukien={self._loaisukien} ngayam={self._ngayam} "
            f"({type(self._ngayam)}) thangam={self._thangam} "
            f"({type(self._thangam)}) namam={self._namam} "
            f"({type(self._namam)}) ngayduong={self._ngayduong} "
            f"({type(self._ngayduong)}) thangduong={self._thangduong} "
            f"({type(self._thangduong)}) namduong={self._namduong} "
            f"({type(self._namduong)})"
        )
        self._attr_unique_id = f"amlichvn_{self._id}"
        self._attr_name = self._tendukien
        self._attr_icon = "mdi:calendar"
        self._state = STATE_UNKNOWN
        self._attr_extra_state_attributes = self._build_attrs()

    def _build_attrs(self):
        # Hiển thị ngày/tháng/năm không có .0 nếu là số nguyên
        if self._loaisukien == "solar":
            ngay = format_int_if_possible(self._ngayduong)
            thang = format_int_if_possible(self._thangduong)
            nam = format_int_if_possible(self._namduong)
            if nam:
                ngay_su_kien = f"{ngay}/{thang}/{nam}"
            else:
                ngay_su_kien = f"{ngay}/{thang}"
        else:
            ngay = format_int_if_possible(self._ngayam)
            thang = format_int_if_possible(self._thangam)
            nam = format_int_if_possible(self._namam)
            if nam:
                ngay_su_kien = f"{ngay}/{thang}/{nam}"
            else:
                ngay_su_kien = f"{ngay}/{thang}"
        attrs = {
            "ngay_su_kien": ngay_su_kien,
            "loai_su_kien": (
                "Duong Lich" if self._loaisukien == "solar" else "Am Lich"
            ),
            "mo_ta": self._mota,
            "laplai": self._laplai
        }
        return attrs

    def _get_nearest_solar(self):
        from datetime import date
        today = date.today()
        try:
            if self._loaisukien == "solar":
                if not self._ngayduong:
                    return None
                sd = int(self._ngayduong)
                if self._laplai == "monthly":
                    month = today.month
                    year = today.year
                    if today.day > sd:
                        month += 1
                        if month > 12:
                            month = 1
                            year += 1
                    return date(year, month, sd)
                elif self._laplai == "yearly":
                    if not self._thangduong:
                        return None
                    month = int(self._thangduong)
                    day = int(self._ngayduong)
                    year = today.year
                    event_date = date(year, month, day)
                    if event_date < today:
                        event_date = date(year+1, month, day)
                    return event_date
                else:
                    if not self._namduong or not self._thangduong:
                        return None
                    year = int(self._namduong)
                    month = int(self._thangduong)
                    day = int(self._ngayduong)
                    return date(year, month, day)
            else:
                try:
                    from lunarcalendar import Converter, Lunar, Solar
                except ImportError:
                    return None
                if not self._ngayam:
                    return None
                lunar_day = int(self._ngayam)
                lunar_month = int(self._thangam) if self._thangam else None
                lunar_year = int(self._namam) if self._namam else today.year
                if self._laplai == "monthly":
                    solar_today = Solar(today.year, today.month, today.day)
                    lunar_today = Converter.Solar2Lunar(solar_today)
                    am_thang = lunar_today.month
                    am_nam = lunar_today.year
                    if lunar_today.day > lunar_day:
                        am_thang += 1
                        if am_thang > 12:
                            am_thang = 1
                            am_nam += 1
                    lunar = Lunar(am_nam, am_thang, lunar_day, False)
                    solar = Converter.Lunar2Solar(lunar)
                    return date(solar.year, solar.month, solar.day)
                elif self._laplai == "yearly":
                    if not lunar_month:
                        return None
                    for offset in [0, 1]:
                        ly = today.year + offset
                        lunar = Lunar(ly, lunar_month, lunar_day, False)
                        solar = Converter.Lunar2Solar(lunar)
                        event_date = date(solar.year, solar.month, solar.day)
                        if event_date >= today:
                            return event_date
                    lunar = Lunar(
                        today.year + 1, lunar_month, lunar_day, False
                    )
                    solar = Converter.Lunar2Solar(lunar)
                    return date(solar.year, solar.month, solar.day)
                else:
                    if not lunar_month:
                        return None
                    lunar = Lunar(lunar_year, lunar_month, lunar_day, False)
                    solar = Converter.Lunar2Solar(lunar)
                    return date(solar.year, solar.month, solar.day)
        except Exception as ex:
            _LOGGER.error(
                "Loi tinh ngay duong gan nhat cho su kien %s: %s",
                self._tendukien,
                ex,
            )
            return None

    def _get_nearest_solar_str(self):
        event_date = self._get_nearest_solar()
        if event_date:
            return event_date.strftime("%d/%m/%Y")
        return ""

    @property
    def state(self):
        from datetime import date
        event_date = self._get_nearest_solar()
        if event_date:
            today = date.today()
            days_left = (event_date - today).days
            return (
                f"Sắp tới {event_date.strftime('%d/%m/%Y')} - "
                f"còn {days_left} ngày"
            )
        return STATE_UNKNOWN

    async def async_update(self):
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, tendukien, loaisukien, ngayam, thangam, namam, "
                "ngayduong, thangduong, namduong, mota, laplai FROM events "
                "WHERE id=?",
                (self._id,)
            )
            row = cursor.fetchone()
            conn.close()
            if row:
                self._tendukien = row[1]
                self._loaisukien = row[2]
                self._ngayam = parse_float_or_none(row[3])
                self._thangam = parse_float_or_none(row[4])
                self._namam = parse_float_or_none(row[5])
                self._ngayduong = parse_float_or_none(row[6])
                self._thangduong = parse_float_or_none(row[7])
                self._namduong = parse_float_or_none(row[8])
                self._mota = row[9]
                self._laplai = row[10]
                self._attr_name = self._tendukien
                self._attr_extra_state_attributes = self._build_attrs()
        except Exception as ex:
            _LOGGER.error(f"Lỗi reload DB cho sensor {self._id}: {ex}")

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, "amlichvn_events")},
            "name": "Âm lịch VN",
            "manufacturer": "amlichvn",
            "model": "Sự kiện Âm/Dương lịch"
        }
