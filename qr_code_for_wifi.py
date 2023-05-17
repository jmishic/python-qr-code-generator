import segno
from segno import helpers


def create_wifi_qr_code(wifi_ssid: str, wifi_password: str, wifi_security: str) -> None:
    config = helpers.make_wifi_data(ssid=wifi_ssid, password=wifi_password, security=wifi_security)
    qr = segno.make(config, error='m')
    qr.save("title-save-as.png", scale=10)


def main() -> None:
    create_wifi_qr_code("wifi ssid", "wifi password", "wifi security")


if __name__ == '__main__':
    main()
