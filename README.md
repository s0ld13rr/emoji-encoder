# Emoji Encoder for Red Team Ops

🚀 **Emoji Encoder** – это инструмент, который позволяет скрывать команды и данные внутри эмодзи с использованием вариационных селекторов Unicode. Подходит для Red Team операций, сокрытия C2-коммуникаций и эксфильтрации данных.

## 🔍 Особенности
- Кодирование произвольных данных в Unicode-вариационные селекторы.
- Декодирование скрытых данных из строки с эмодзи.
- Возможность исполнения скрытых команд на целевой системе.

## ⚡ Установка
```bash
git clone https://github.com/yourrepo/emoji-encoder.git
cd emoji-encoder
```

## 📌 Использование
### Кодирование данных
```python
from emoji_encoder import encode

emoji_text = encode("ping")
print(emoji_text)  # 🔥󠅐󠅉󠅎󠅇
```

### Декодирование данных
```python
from emoji_encoder import decode

decoded_text = decode("🔥󠅐󠅉󠅎󠅇")
print(decoded_text)  # ping
```

### Исполнение команд
```python
from emoji_encoder import execute_command

output = execute_command("🔥󠅄󠅉󠅒")  # скрытая команда dir
print(output)
```

## ⚠️ Дисклеймер
Этот инструмент предназначен исключительно для учебных и исследовательских целей. Использование его в нелегальных или несанкционированных целях запрещено.

---

📢 **Связь и обновления:** Подписывайтесь на @s0ld13r_ch

