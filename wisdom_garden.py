#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
지혜의 정원 (Wisdom Garden)
An Interactive Exploration of "I Know Nothing"

A beautiful, interactive program that grows a garden of wisdom
through questions and reflection.
"""

import random
import time
import sys


def clear_screen():
    """Clear the screen"""
    print("\n" * 2)


def print_slow(text, delay=0.03):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def draw_garden(wisdom_seeds):
    """Draw a beautiful ASCII garden that grows with wisdom"""
    clear_screen()
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 18 + "🌸 지혜의 정원 🌸" + " " * 18 + "║")
    print("║" + " " * 18 + "(Wisdom Garden)" + " " * 20 + "║")
    print("╚" + "═" * 58 + "╝")
    print()
    
    # Garden visualization
    garden_levels = [
        ["     ", "  🌱  ", "  🌿  ", "  🌺  ", "  🌸  ", "  🌻  "],  # Growth stages
    ]
    
    print("  " + "─" * 54)
    
    # Draw garden rows
    for row in range(3):
        line = "  │ "
        for col in range(5):
            idx = row * 5 + col
            if idx < len(wisdom_seeds):
                stage = min(wisdom_seeds[idx], 5)
                line += garden_levels[0][stage]
            else:
                line += "     "
        line += " │"
        print(line)
    
    print("  " + "─" * 54)
    print(f"\n  🌱 심어진 지혜의 씨앗: {len(wisdom_seeds)}개")
    print(f"  (Wisdom seeds planted: {len(wisdom_seeds)})\n")


def wisdom_seed_question(question_num):
    """Ask a philosophical question and plant a wisdom seed"""
    questions = [
        {
            "ko": "당신은 진정으로 무엇을 알고 있나요?",
            "en": "What do you truly know?",
            "wisdom": "질문하는 것 자체가 지혜의 시작입니다."
        },
        {
            "ko": "모르는 것을 인정하는 것이 왜 두려운가요?",
            "en": "Why is it scary to admit what we don't know?",
            "wisdom": "두려움을 인정하면 용기가 자랍니다."
        },
        {
            "ko": "지식과 지혜의 차이는 무엇일까요?",
            "en": "What is the difference between knowledge and wisdom?",
            "wisdom": "지식은 쌓이지만, 지혜는 자랍니다."
        },
        {
            "ko": "당신이 가장 배우고 싶은 것은 무엇인가요?",
            "en": "What do you most want to learn?",
            "wisdom": "배움의 욕구는 무지를 인정하는 것에서 시작됩니다."
        },
        {
            "ko": "실수는 정말 나쁜 것일까요?",
            "en": "Are mistakes really bad?",
            "wisdom": "실수는 성장의 씨앗입니다."
        },
        {
            "ko": "완벽함이란 무엇일까요?",
            "en": "What is perfection?",
            "wisdom": "불완전함을 받아들이는 것이 완벽에 가까운 것입니다."
        },
        {
            "ko": "다른 사람의 관점에서 세상을 본 적이 있나요?",
            "en": "Have you ever seen the world from someone else's perspective?",
            "wisdom": "다른 눈으로 보면 새로운 세상이 열립니다."
        },
        {
            "ko": "침묵이 때로는 말보다 강할까요?",
            "en": "Can silence be more powerful than words?",
            "wisdom": "때로는 말하지 않는 것이 가장 큰 지혜입니다."
        },
        {
            "ko": "어제의 당신과 오늘의 당신은 같은 사람인가요?",
            "en": "Are you the same person today as you were yesterday?",
            "wisdom": "변화는 삶의 유일한 상수입니다."
        },
        {
            "ko": "행복은 목적지인가요, 여정인가요?",
            "en": "Is happiness a destination or a journey?",
            "wisdom": "지금 이 순간이 바로 행복입니다."
        },
    ]
    
    if question_num < len(questions):
        q = questions[question_num]
    else:
        q = random.choice(questions)
    
    print("\n" + "─" * 60)
    print(f"💭 질문 {question_num + 1}:")
    print(f"   {q['ko']}")
    print(f"   ({q['en']})")
    print("─" * 60)
    
    answer = input("\n➤ 당신의 생각: ")
    
    print()
    print_slow(f"✨ {q['wisdom']}", 0.02)
    print()
    time.sleep(1)
    
    return len(answer) > 0


def philosophical_moments():
    """Share beautiful philosophical moments"""
    moments = [
        ("🌊", "물처럼 되어라. 형태가 없지만 모든 형태를 담을 수 있다.", 
         "Be like water. Formless, yet capable of taking any form."),
        ("🍃", "바람에 흔들리는 나무는 부러지지 않는다.", 
         "The tree that bends in the wind does not break."),
        ("🌙", "어둠이 있어야 별이 빛난다.", 
         "Stars only shine in darkness."),
        ("🦋", "나비는 자신이 애벌레였음을 기억할까?", 
         "Does the butterfly remember being a caterpillar?"),
        ("🌅", "매일 아침은 새로운 시작이다.", 
         "Every morning is a new beginning."),
    ]
    
    emoji, korean, english = random.choice(moments)
    print(f"\n{emoji}  {korean}")
    print(f"    ({english})\n")
    time.sleep(2)


def growing_animation():
    """Show seeds growing animation"""
    stages = ["🌱", "🌿", "🌺", "🌸", "🌻", "✨"]
    print("\n" + " " * 20, end="")
    for stage in stages:
        print(f"\r" + " " * 20 + stage + " 지혜가 자라고 있습니다...", end="", flush=True)
        time.sleep(0.3)
    print()
    time.sleep(0.5)


def final_wisdom_message(seeds_count):
    """Display final wisdom message"""
    clear_screen()
    print()
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + " " * 12 + "🌸 지혜의 정원이 완성되었습니다 🌸" + " " * 12 + "║")
    print("║" + " " * 12 + "  (Your Wisdom Garden is Complete)  " + " " * 12 + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "═" * 58 + "╝")
    print()
    
    print(f"  당신은 {seeds_count}개의 지혜 씨앗을 심었습니다. 🌱")
    print(f"  (You have planted {seeds_count} wisdom seeds.)")
    print()
    
    wisdom_messages = [
        "진정한 지혜는 모르는 것을 아는 데서 시작됩니다.",
        "당신의 질문 하나하나가 아름다운 꽃으로 피어났습니다.",
        "무지를 인정하는 용기가 당신을 더 현명하게 만들었습니다.",
    ]
    
    for msg in wisdom_messages:
        print(f"  ✨ {msg}")
        time.sleep(1)
    
    print()
    print("  " + "─" * 54)
    print()
    print("  💫 기억하세요:")
    print_slow("     나는 아무것도 모른다... 그래서 무한히 배울 수 있다!", 0.02)
    print_slow("     I know nothing... so I can learn infinitely!", 0.02)
    print()
    print("  " + "─" * 54)
    print()


def main():
    """Main function"""
    clear_screen()
    
    # Welcome message
    print("\n")
    print("  ╔" + "═" * 56 + "╗")
    print("  ║" + " " * 56 + "║")
    print("  ║" + " " * 8 + "🌸 지혜의 정원에 오신 것을 환영합니다 🌸" + " " * 8 + "║")
    print("  ║" + " " * 12 + "(Welcome to the Wisdom Garden)" + " " * 13 + "║")
    print("  ║" + " " * 56 + "║")
    print("  ╚" + "═" * 56 + "╝")
    print()
    print_slow("  이곳에서 당신은 '아무것도 모른다'는 것의 아름다움을 발견할 것입니다.", 0.02)
    print_slow("  Here you will discover the beauty of 'knowing nothing'.", 0.02)
    print()
    
    input("  ✨ 엔터를 눌러 시작하세요... (Press Enter to begin...) ")
    
    wisdom_seeds = []
    
    # Plant 5 wisdom seeds through questions
    for i in range(5):
        draw_garden(wisdom_seeds)
        philosophical_moments()
        
        if wisdom_seed_question(i):
            growing_animation()
            wisdom_seeds.append(random.randint(1, 5))
            print(f"\n  🌱 새로운 지혜의 씨앗이 심어졌습니다! (Wisdom seed planted!)")
            time.sleep(1)
    
    # Show final garden
    draw_garden(wisdom_seeds)
    time.sleep(2)
    
    # Final message
    final_wisdom_message(len(wisdom_seeds))
    
    print("\n  🙏 함께해주셔서 감사합니다!")
    print("     Thank you for joining this journey!\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  🌸 언제든 다시 돌아오세요... (Come back anytime...)\n")
    except Exception as e:
        print(f"\n  ⚠️  오류가 발생했습니다: {e}")
        print("     하지만 실수도 배움의 일부입니다! 🌟\n")
