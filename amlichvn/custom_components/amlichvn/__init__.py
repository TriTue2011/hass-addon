import logging

from .const import DOMAIN
from homeassistant.helpers.event import async_track_time_change
from homeassistant.core import callback

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass, config):
    return True


async def async_setup_entry(hass, entry):
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = {}
    await hass.config_entries.async_forward_entry_setups(
        entry, ["sensor", "calendar"]
    )

    # Đăng ký callback để cập nhật dữ liệu mỗi ngày lúc 0h
    @callback
    async def midnight_update(now):
        _LOGGER.info("AmLichVN: Đang cập nhật dữ liệu lúc 0h")

    async_track_time_change(
        hass,
        midnight_update,
        hour=0,
        minute=0,
        second=10,
    )

    # Đăng ký service để reload entry (có thể gọi từ code khác)
    async def reload_entry_service(call):
        _LOGGER.info("AmLichVN: Reloading config entry by service")
        await hass.config_entries.async_reload(entry.entry_id)

    hass.services.async_register(DOMAIN, "reload_entry", reload_entry_service)

    return True


async def async_unload_entry(hass, entry):
    await hass.config_entries.async_forward_entry_unload(entry, "calendar")
    return await hass.config_entries.async_forward_entry_unload(
        entry, "sensor"
    )
