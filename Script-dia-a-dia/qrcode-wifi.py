import qrcode
from PIL import Image, ImageDraw, ImageFont

# Informações do WiFi
ssid = "Wifi"
password = "s12345678"
encryption = "WPA"
bssid = "AA:BB:CC:DD:EE:FF"  # Endereço MAC do AP

# Formatação da string para QR code
wifi_config = f"WIFI:T:{encryption};S:{ssid};P:{password};;"

# Gerar QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(wifi_config)
qr.make(fit=True)

img_qr = qr.make_image(fill_color="black", back_color="white")

# Adicionar instruções ao QR code
instrucao = f"Certifique-se de que o BSSID seja {bssid} antes de conectar."
fonte = ImageFont.load_default()  # Fonte padrão do PIL

# Carregar o logo da empresa
logo = Image.open("IMAGEM-AQUI.png")  # Certifique-se de ter um arquivo 'IMAGEM-AQUI.png' no mesmo diretório
logo_largura = 100  # Definir a largura desejada para o logo
proporcao = logo.size[1] / logo.size[0]
logo_altura = int(logo_largura * proporcao)
logo = logo.resize((logo_largura, logo_altura))

largura, altura = img_qr.size
altura_total = altura + 100 + 50  # Espaço extra para as instruções e o logo

imagem_final = Image.new('RGB', (largura, altura_total), 'white')
imagem_final.paste(img_qr, (0, 0))

# Adicionar o logo abaixo do QR Code
posicao_logo = ((largura - logo_largura) // 2, altura + 10)
imagem_final.paste(logo, posicao_logo, logo)  # O terceiro parâmetro é a máscara do logo para lidar com a transparência


draw = ImageDraw.Draw(imagem_final)
draw.text((10, altura + logo_altura + 20), instrucao, font=fonte, fill="black")


imagem_final.save("wifi_qr_code_com_instrucao_e_logo.png")

print("QR code com instrução e logo gerado e salvo como 'wifi_qr_code_com_instrucao_e_logo.png'")
