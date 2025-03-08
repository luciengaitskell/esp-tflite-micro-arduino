Import("env")


def add_filters(filters, mcu, expected_mcu):
    if expected_mcu not in mcu:
        print(f"Excluding {expected_mcu.upper()} specific ESP-NN files.")
        filters.extend([f"-<**/*{expected_mcu}.c>", f"-<**/*{expected_mcu}.S>"])
    else:
        print(f"Including {expected_mcu.upper()} specific ESP-NN files.")


def modify_lib_src_filter():
    # Retrieve the MCU type from board configuration
    mcu = env.BoardConfig().get("build.mcu", "").lower()
    print("Current MCU:", mcu)

    filters = ["+<**/*.c>", "+<**/*.S>"]

    for expected_mcu in ["esp32s3", "esp32p4"]:
        add_filters(filters, mcu, expected_mcu)

    env.Replace(SRC_FILTER=filters)


# print(env.Dump())
modify_lib_src_filter()
