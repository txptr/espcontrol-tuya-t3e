# EspControl Tuya T3E

480x480 square ESP32-S3 panel running EspControl.

This is a **template repository** — a standalone device package for the EspControl smart home control system.

## Quick Start

### Prerequisites

- **ESPHome CLI** — [install guide](https://esphome.io/guides/installing_esphome.html)
- **Python 3.8+** — usually included with ESPHome
- **USB-C cable** — for flashing firmware to the device
- **2.4 GHz WiFi** — for device connectivity

### Build & Flash

#### 1. Clone this repository

```bash
git clone https://github.com/YOUR_USERNAME/espcontrol-tuya-t3e
cd espcontrol-tuya-t3e
```

#### 2. Generate the web UI bundle

```bash
python3 scripts/build_www.py
```

This creates `docs/public/webserver/tuya-t3e/www.js` — the interface users will interact with on their device.

#### 3. Connect your device via USB and flash

```bash
esphome run devices/tuya-t3e/esphome.yaml
```

ESPHome will:
- Compile the firmware
- Detect your USB device
- Flash the binary
- Show you logs in real-time

Select your USB device when prompted (usually `/dev/ttyUSB0` on Linux or `COM*` on Windows).

#### 4. First Boot

The device will boot into a setup screen:

1. **WiFi Setup** — Enter your 2.4 GHz WiFi credentials
2. **Home Assistant Setup** — Give permission for the device to control your entities
3. **Configuration** — Choose which controls appear on the screen

After setup, the device will restart and show the main control grid.

---

## Device Specifications

| Property | Value |
|----------|-------|
| **Display** | 480×480 square IPS TFT (ST7701S) |
| **MCU** | ESP32-S3 (6-core, 16 MB flash) |
| **RAM** | 8 MB PSRAM |
| **Touch Input** | GT911 capacitive touchscreen |
| **Connectivity** | 2.4 GHz 802.11 b/g/n WiFi |
| **Backlight** | PWM-controlled 3.3V LED (GPIO 2) |
| **Grid Layout** | 3×3 buttons (9 slots) |
| **Power** | USB-C (5V typical, requires ~2A) |

---

## Usage

### Configure Controls from the Web UI

1. Open `http://<device-ip>` in your browser
2. Drag buttons to rearrange them
3. Click buttons to assign Home Assistant entities
4. Choose icons, labels, and colors
5. Click **Save** — configuration syncs to the device in seconds

### Available Control Types

- **Lights** — brightness, color, color temperature
- **Switches** — toggle on/off
- **Fans** — speed control, direction
- **Climate** — temperature, mode, fan speed
- **Covers** — blinds, shutters, garage doors
- **Media Players** — play/pause, volume, album art
- **Sensors** — temperature, humidity, battery, custom text
- **Scenes & Scripts** — run automations with one tap
- **Weather** — forecast, current conditions
- **Clocks & Dates** — display time, date, world clock
- **Alarms** — set alarms directly on device

### Display Settings

From the web UI, customize:

- **Active Color** — button highlight color when pressed
- **Rotation** — 0°, 90°, 180°, 270°
- **Brightness Schedule** — dim at night, full brightness during day
- **Idle Sleep** — turn off display when not in use
- **Language** — English, German, French, Spanish (see [docs](https://jtenniswood.github.io/espcontrol/))

---

## Customization

### Modify Hardware Pins

Edit `devices/tuya-t3e/device/device.yaml` to change GPIO assignments:

```yaml
output:
  - platform: ledc
    id: backlight_pwm
    pin: GPIO2           # Change to your backlight pin
    frequency: 20kHz
```

After changes, rebuild and flash:

```bash
esphome run devices/tuya-t3e/esphome.yaml
```

### Adjust Display Parameters

In `devices/tuya-t3e/packages.yaml`, modify substitutions like:

```yaml
substitutions:
  screen_width: "480"
  screen_height: "480"
  padding: 14px         # Space around cards
  radius: 8px           # Button corner radius
```

---

## Troubleshooting

### "No matching device found" during flash

**Check:**
- USB cable is plugged in (try a different cable)
- Device is powered and switched on
- Run `esphome logs devices/tuya-t3e/esphome.yaml` to check USB detection

### WiFi connection fails

**Check:**
- Device is in WiFi setup screen
- WiFi password is correct (case-sensitive)
- Router broadcasts 2.4 GHz (not 5 GHz only)
- Signal strength is good (move device closer if needed)

### Web UI doesn't load at `http://device-ip`

**Check:**
- Device is on the same WiFi network
- Find device IP: Open Home Assistant → Devices → EspControl
- Try `http://espcontrol-tuya-t3e.local` instead of IP address

### Buttons don't control devices

**Check:**
- Device is added to Home Assistant (should appear automatically after WiFi setup)
- Home Assistant can reach the device (check integration logs)
- Entities exist in Home Assistant (they should appear in the entity picker)

---

## Documentation

- **Main EspControl Docs** — [jtenniswood.github.io/espcontrol](https://jtenniswood.github.io/espcontrol/)
- **FAQ** — [jtenniswood.github.io/espcontrol/reference/faq](https://jtenniswood.github.io/espcontrol/reference/faq)
- **ESPHome Docs** — [esphome.io](https://esphome.io/)

---

## Updates

### Keep EspControl Updated

When the main EspControl repository updates with new features or bug fixes, you can pull them into your device:

```bash
# From the espcontrol-tuya-t3e directory:
git pull origin main

# Rebuild if any espcontrol components changed:
esphome run devices/tuya-t3e/esphome.yaml
```

---

## License

This device template is part of EspControl, licensed under the [PolyForm Noncommercial License 1.0.0](https://polyformproject.org/licenses/noncommercial/1.0.0/).

**In plain terms:** You can use, modify, and share this software for non-commercial purposes. Commercial use requires permission from the EspControl maintainer.

---

## Support & Feedback

- **Issues with the Tuya T3E device** — Open an issue in this repository
- **Issues with EspControl features** — See [main EspControl repository](https://github.com/jtenniswood/espcontrol)
- **ESPHome questions** — [ESPHome Discord](https://discord.gg/esphome)

---

## Credits

- **EspControl** — [jtenniswood/espcontrol](https://github.com/jtenniswood/espcontrol)
- **ESPHome** — [esphome/esphome](https://github.com/esphome/esphome)
- **LVGL** — [lvgl/lvgl](https://github.com/lvgl/lvgl)
