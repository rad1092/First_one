#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
나는 아무것도 모른다 - 런처 (I Know Nothing - Launcher)

Choose which philosophical journey you want to embark on!
"""

import sys
import os


def print_banner():
    """Print the main banner"""
    print("\n" + "═" * 70)
    print("║" + " " * 68 + "║")
    print("║" + " " * 16 + "🧠 나는 아무것도 모른다 🧠" + " " * 21 + "║")
    print("║" + " " * 20 + "(I Know Nothing)" + " " * 26 + "║")
    print("║" + " " * 68 + "║")
    print("║" + " " * 12 + "A Philosophical Journey in Python" + " " * 21 + "║")
    print("║" + " " * 68 + "║")
    print("═" * 70)
    print()


def main():
    """Main launcher"""
    print_banner()
    
    print("어떤 철학적 여정을 시작하시겠습니까?")
    print("(Which philosophical journey would you like to begin?)\n")
    
    print("1. 🌸 지혜의 정원 (Wisdom Garden)")
    print("   → 인터랙티브하고 아름다운 지혜 성장 경험")
    print("   → Interactive and beautiful wisdom-growing experience\n")
    
    print("2. 🧠 지식의 역설 (Knowledge Paradox)")
    print("   → 소크라테스 철학의 깊은 탐구")
    print("   → Deep exploration of Socratic philosophy\n")
    
    print("0. 종료 (Exit)\n")
    
    choice = input("선택하세요 (Choose): ").strip()
    
    if choice == "1":
        print("\n🌸 지혜의 정원으로 안내합니다...\n")
        os.system("python3 wisdom_garden.py")
    elif choice == "2":
        print("\n🧠 지식의 역설 여정을 시작합니다...\n")
        os.system("python3 i_know_nothing.py")
    elif choice == "0":
        print("\n✨ 안녕히 가세요! (Goodbye!)\n")
    else:
        print("\n❌ 잘못된 선택입니다. (Invalid choice.)")
        print("다시 시도해주세요. (Please try again.)\n")
        main()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✨ 프로그램을 종료합니다... (Exiting...)\n")
    except Exception as e:
        print(f"\n⚠️  오류: {e}\n")
