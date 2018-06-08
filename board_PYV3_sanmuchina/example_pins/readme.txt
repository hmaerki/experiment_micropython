https://github.com/micropython/micropython/blob/master/examples/pins.py

pins_af.py wurde aus dem entsprechenden Buildverzeichnis kopiert


>>> pins.af()
B13       1: TIM1_CH1N   5: SPI2_SCK    5: I2S2_CK     7: USART3_CTS  9: CAN2_TX
B14       1: TIM1_CH2N   3: TIM8_CH2N   5: SPI2_MISO   6: I2S2_EXTSD  7: USART3_RTS  9: TIM12_CH1
B15       1: TIM1_CH3N   3: TIM8_CH3N   5: SPI2_MOSI   5: I2S2_SD     9: TIM12_CH2
C6        2: TIM3_CH1    3: TIM8_CH1    5: I2S2_MCK    8: USART6_TX
C7        2: TIM3_CH2    3: TIM8_CH2    6: I2S3_MCK    8: USART6_RX
A13
A14
A15       1: TIM2_CH1    1: TIM2_ETR    5: SPI1_NSS    6: SPI3_NSS    6: I2S3_WS
B3        1: TIM2_CH2    5: SPI1_SCK    6: SPI3_SCK    6: I2S3_CK
B4        2: TIM3_CH1    5: SPI1_MISO   6: SPI3_MISO   7: I2S3_EXTSD
B6        2: TIM4_CH1    4: I2C1_SCL    7: USART1_TX   9: CAN2_TX
B7        2: TIM4_CH2    4: I2C1_SDA    7: USART1_RX
B8        2: TIM4_CH3    3: TIM10_CH1   4: I2C1_SCL    9: CAN1_RX
B9        2: TIM4_CH4    3: TIM11_CH1   4: I2C1_SDA    5: SPI2_NSS    5: I2S2_WS     9: CAN1_TX
C0
C1
C2        5: SPI2_MISO   6: I2S2_EXTSD
C3        5: SPI2_MOSI   5: I2S2_SD
A0        1: TIM2_CH1    1: TIM2_ETR    2: TIM5_CH1    3: TIM8_ETR    7: USART2_CTS  8: UART4_TX
A1        1: TIM2_CH2    2: TIM5_CH2    7: USART2_RTS  8: UART4_RX
A2        1: TIM2_CH3    2: TIM5_CH3    3: TIM9_CH1    7: USART2_TX
A3        1: TIM2_CH4    2: TIM5_CH4    3: TIM9_CH2    7: USART2_RX
A4        5: SPI1_NSS    6: SPI3_NSS    6: I2S3_WS     7: USART2_CK
A5        1: TIM2_CH1    1: TIM2_ETR    3: TIM8_CH1N   5: SPI1_SCK
A6        1: TIM1_BKIN   2: TIM3_CH1    3: TIM8_BKIN   5: SPI1_MISO   9: TIM13_CH1
A7        1: TIM1_CH1N   2: TIM3_CH2    3: TIM8_CH1N   5: SPI1_MOSI   9: TIM14_CH1
B0        1: TIM1_CH2N   2: TIM3_CH3    3: TIM8_CH2N
B1        1: TIM1_CH3N   2: TIM3_CH4    3: TIM8_CH3N
B10       1: TIM2_CH3    4: I2C2_SCL    5: SPI2_SCK    5: I2S2_CK     7: USART3_TX
B11       1: TIM2_CH4    4: I2C2_SDA    7: USART3_RX
B12       1: TIM1_BKIN   5: SPI2_NSS    5: I2S2_WS     7: USART3_CK   9: CAN2_RX
LED_R1    1: TIM1_CH1    4: I2C3_SCL    7: USART1_CK
LED_R2    1: TIM1_CH3    7: USART1_RX
LED_G1
LED_G2
SW
SD
MMA_INT
MMA_AVDD  2: TIM3_CH2    5: SPI1_MOSI   6: SPI3_MOSI   6: I2S3_SD     9: CAN2_RX
SD_D0     2: TIM3_CH3    3: TIM8_CH3    8: USART6_CK
SD_D1     2: TIM3_CH4    3: TIM8_CH4    4: I2C3_SDA
SD_D2     6: SPI3_SCK    6: I2S3_CK     7: USART3_TX   8: UART4_TX
SD_D3     5: I2S3_EXTSD  6: SPI3_MISO   7: USART3_RX   8: UART4_RX
SD_CK     6: SPI3_MOSI   6: I2S3_SD     7: USART3_CK   8: UART5_TX
SD_CMD    2: TIM3_ETR    8: UART5_RX
UART1_TX  1: TIM1_CH2    7: USART1_TX
USB_DM    1: TIM1_CH4    7: USART1_CTS  9: CAN1_RX
USB_DP    1: TIM1_ETR    7: USART1_RTS  9: CAN1_TX


>>> pins.pins()
B13      IN
B14      IN
B15      IN
C6       IN
C7       IN
A13      IN     PULL_UP
A14      AF_PP  PULL_DOWN 0
A15      AF_PP  PULL_UP   0
B3       AF_PP            0
B4       AF_PP  PULL_UP   0
B6       IN
B7       IN
B8       AF_PP  PULL_UP   9: CAN1_RX
B9       AF_PP  PULL_UP   9: CAN1_TX
C0       IN
C1       IN
C2       IN
C3       IN
A0       IN
A1       IN
A2       IN
A3       IN
A4       IN
A5       IN
A6       IN
A7       IN
B0       IN
B1       IN
B10      IN
B11      IN
B12      IN
LED_R1   OUT_PP
LED_R2   OUT_PP
LED_G1   OUT_PP
LED_G2   OUT_PP
SW       IN     PULL_UP
SD       IN     PULL_DOWN
MMA_INT  IN
MMA_AVDD OUT_PP
SD_D0    AF_PP  PULL_UP   12
SD_D1    AF_PP  PULL_UP   12
SD_D2    AF_PP  PULL_UP   12
SD_D3    AF_PP  PULL_UP   12
SD_CK    AF_PP  PULL_UP   12
SD_CMD   AF_PP  PULL_UP   12
UART1_TX IN
USB_DM   AF_PP            10
USB_DP   AF_PP            10



