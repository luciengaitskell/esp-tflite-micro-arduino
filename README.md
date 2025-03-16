`esp-tflite-micro-arduino`

## Demo for ESP32 cameras with TFLite

```bash
# Build
pio run
# Build and upload
pio run --target upload
```

## Boards

### ESP32-CAM

https://docs.platformio.org/en/stable/boards/espressif32/esp32cam.html

```bash
pio run -e esp32cam
```

## XIAO ESP32-S3 Sense

https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/

```bash
pio run -e xiaoesp32s3
```

## Libraries

The project uses two libraries for tflite functionality,
which are included as git submodules in the `lib` directory.
I have added `library.json` files above the submodules to allow for PlatformIO configuration.

- https://github.com/espressif/esp-tflite-micro
  - TensorFlow Lite for Microcontrollers,
    modified for ESP32 with calls to `esp-nn` optimized kernels (when enabled).
- https://github.com/espressif/esp-nn
  - optimized kernels for ESP32, ESP32-S3, and ESP32-P4.
