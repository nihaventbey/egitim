#!/usr/bin/env python
import os
import sys

def main():
    """Django komut satırı arayüzü"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'egitim.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django yüklü değil veya sanal ortam aktif değil."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
