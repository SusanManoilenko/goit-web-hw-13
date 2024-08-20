import os
import locale

# Примусове встановлення UTF-8
os.environ['PYTHONIOENCODING'] = 'utf-8'

# Перевірка поточного кодування
print(locale.getpreferredencoding())