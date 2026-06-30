# EspControl Tuya T3E

480x480 square ESP32-S3 panel running EspControl.

This is a **standalone device template** for the EspControl smart home control system. No forking, no maintainer involvement — just clone and build!

## Quick Start (ESPHome WiFi Flashing)

### Prerequisites

- **Home Assistant** with ESPHome add-on (recommended) or **ESPHome CLI**
- **WiFi credentials** for 2.4 GHz network
- **GitHub account** (free tier works fine)

### Setup in 5 Steps

#### 1️⃣ Copy Configuration Template

Copy the content of `esphome-template.yaml` to your ESPHome config:

**If using ESPHome via Home Assistant:**
- Open Home Assistant → Settings → Devices & Services → ESPHome
- Click "+ Create New Device"
- Paste the template content
- Update `YOUR_GITHUB_USERNAME` to your GitHub username
- Save as `tuya-t3e.yaml`

**If using ESPHome CLI:**
```bash
cp esphome-template.yaml ~/esphome/tuya-t3e.yaml
```

#### 2️⃣ Create Secrets File

Create `secrets.yaml` in your ESPHome config directory:

```yaml
wifi_ssid: "Your WiFi Network"
wifi_password: "Your WiFi Password"
api_encryption_key: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
ota_password: "your-ota-password"
```

(See `secrets-template.yaml` for full template)

#### 3️⃣ First Time: Flash via USB

Connect device to computer via USB-C and flash:

**Home Assistant ESPHome add-on:**
- Click the three dots on your device
- Select "Install" → "Plug into computer running the browser"
- Follow the browser prompts to flash

**ESPHome CLI:**
```bash
esphome run tuya-t3e.yaml
```

#### 4️⃣ Configure WiFi (On Device)

After first flash, device boots into setup screen:
- Follow on-device WiFi setup screen
- Enter your 2.4 GHz credentials
- Device connects to WiFi

#### 5️⃣ All Future Updates: WiFi Only

After first setup, everything is wireless:

**Home Assistant ESPHome:**
- Click "Install" → "Wirelessly"
- Device flashes over WiFi in ~2 minutes

**ESPHome CLI:**
```bash
esphome run tuya-t3e.yaml
```

---

## How It Works

```
Your ESPHome Config
        ↓
   tuya-t3e.yaml (includes packages.yaml from this repo)
        ↓
   ├─ Hardware config (device.yaml, fonts, display)
   ├─ ESPHome components (from github.com/jtenniswood/espcontrol)
   └─ Web UI (www.js built automatically via GitHub Actions)
        ↓
   Firmware compiles and flashes
```

**Key:** This repo provides everything except your WiFi credentials. When you update this repo, your devices automatically get the latest features and bug fixes.

---

## Device Specifications

| Property | Value |
|----------|-------|
| **Display** | 480×480 square IPS TFT (ST7701S RGB) |
| **MCU** | ESP32-S3 (6-core, 240 MHz, 16 MB flash) |
| **RAM** | 8 MB PSRAM |
| **Touch** | GT911 capacitive touchscreen |
| **WiFi** | 802.11 b/g/n 2.4 GHz (no 5 GHz) |
| **Backlight** | PWM dimmable (GPIO 2) |
| **Grid** | 3×3 buttons (9 controllable slots) |
| **Power** | USB-C 5V ~2A typical |
| **Rotation** | Software rotatable: 0°, 90°, 180°, 270° |

---

## After Setup: Configure Your Controls

Once device is added to Home Assistant:

1. **Open web UI:** `http://<device-ip>` or Home Assistant → Devices → Your device
2. **Drag to rearrange** buttons
3. **Click buttons** to assign Home Assistant entities (lights, switches, sensors, etc.)
4. **Save** — changes sync to device in seconds

### Supported Controls

- **Lights** — brightness, color, color temperature
- **Switches** — simple on/off
- **Fans** — speed, direction, oscillation
- **Climate** — temperature, mode, humidity
- **Covers** — blinds, shutters, garage doors
- **Media** — play/pause, volume, album art display
- **Sensors** — temperature, humidity, battery, custom text
- **Scenes & Scripts** — one-tap automations
- **Weather** — forecasts, current conditions
- **Time** — clocks, dates, timezones
- **Alarms** — direct device control

---

## Customization

### Change Hardware Pins

Edit `devices/tuya-t3e/device/device.yaml`:

```yaml
output:
  - platform: ledc
    id: backlight_pwm
    pin: GPIO2  # ← Change pin here
```

Rebuild and re-flash via WiFi.

### Adjust Display Appearance

In your `tuya-t3e.yaml`, add substitutions:

```yaml
substitutions:
  name: "my-device"
  padding: 14px        # Space around buttons
  radius: 8px          # Corner radius
  main_page_card_gap: "10"  # Button spacing
```

---

## Updates

### Keep Your Device Updated

When this repository updates with new features or bug fixes:

```bash
# For Home Assistant: Just re-flash wirelessly (click "Install" → "Wirelessly")
# For CLI: esphome run tuya-t3e.yaml
```

The device automatically fetches the latest `www.js` from GitHub Pages.

### What Gets Updated?

- ✅ Web UI features and bug fixes
- ✅ Firmware improvements (display, controls, Home Assistant integration)
- ✅ New control types and card options
- ❌ Your WiFi settings or custom configurations (saved on device)

---

## Troubleshooting

### First Flash: "No devices found"

- Check USB cable (try different cable)
- Try browser on different computer
- On Linux: `ls /dev/ttyUSB*` should show your device

### Device won't connect to WiFi

- 2.4 GHz network required (5 GHz won't work)
- Try moving closer to router
- Reboot device (power cycle)
- Check WiFi password (case-sensitive)

### Web UI shows but buttons don't work

- Device must be in same WiFi network as Home Assistant
- Check if device is added to Home Assistant
- Verify Home Assistant can reach the device IP

### WiFi flashing says "Encryption required"

Generate API encryption key:

```bash
esphome logs tuya-t3e.yaml
```

Copy the generated key into `secrets.yaml` under `api_encryption_key`.

---

## Building from Source (Advanced)

If you want to build locally without ESPHome:

```bash
# Generate www.js
python3 scripts/build_www.py

# Then use esphome.yaml from devices/tuya-t3e/ instead of template
esphome run devices/tuya-t3e/esphome.yaml
```

---

## Documentation

- **EspControl Docs** — https://jtenniswood.github.io/espcontrol/
- **ESPHome Docs** — https://esphome.io/
- **Home Assistant Docs** — https://www.home-assistant.io/
- **GitHub Actions Status** — https://github.com/YOUR_USERNAME/espcontrol-tuya-t3e/actions

---

## Support

- **Issues with Tuya T3E device** — Open an issue in this repository
- **General EspControl questions** — See [main EspControl repo](https://github.com/jtenniswood/espcontrol)
- **ESPHome support** — [ESPHome Discord](https://discord.gg/esphome)

---

## License

Licensed under **PolyForm Noncommercial License 1.0.0** (same as EspControl).

**Plain English:** You can use, modify, and share for non-commercial purposes. Commercial use requires permission from the EspControl maintainer.

See [LICENSE](LICENSE) file for full terms.

---

## How This Compares to Forking

| | Your Repo | Forked espcontrol |
|---|-----------|-------------------|
| **Setup** | 5 minutes | Manual merges, keep in sync |
| **Updates** | Automatic (GitHub Actions) | Manual git pulls |
| **Maintenance** | Zero from maintainer | Burden on maintainer |
| **Hardware variations** | Easy (just change device.yaml) | Needs permission to add |
| **www.js** | Auto-built on GitHub | Manually generated |

This template approach means the EspControl maintainer can stay focused on the core project, while you own and maintain your device variant. Win-win! 🎉

---

## Credits

- **EspControl** — [jtenniswood/espcontrol](https://github.com/jtenniswood/espcontrol)
- **ESPHome** — [esphome/esphome](https://github.com/esphome/esphome)
- **LVGL** — [lvgl/lvgl](https://github.com/lvgl/lvgl)
- **Material Design Icons** — [materialdesignicons.com](https://materialdesignicons.com/)
