#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
나는 아무것도 모른다 (I Know Nothing)
A Philosophical Journey into the Paradox of Knowledge

Inspired by Socrates: "I know that I know nothing"
"""

import random
import time
import sys


class KnowledgeParadox:
    """Explores the philosophical concept of knowing nothing"""
    
    def __init__(self):
        self.wisdom_level = 0
        self.questions_asked = 0
        
    def display_ascii_art(self):
        """Display beautiful ASCII art"""
        art = r"""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║      나는 아무것도 모른다                                  ║
║      (I Know That I Know Nothing)                        ║
║                                                          ║
║           🧠  A Philosophical Journey  🧠                ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

        .------.
       /        \
      |  O    O  |     "The only true wisdom
      |     >    |      is in knowing you
      |   \__/   |      know nothing."
       \        /       
        `------'              - Socrates
        """
        print(art)
        
    def animate_text(self, text, delay=0.03):
        """Animate text character by character"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
        
    def display_philosophical_quotes(self):
        """Display various philosophical quotes about knowledge"""
        quotes = [
            "나는 아무것도 모른다... 하지만 그것을 안다는 건 무언가를 아는 것이 아닐까?",
            "The more I learn, the more I realize how much I don't know.",
            "知之為知之，不知為不知，是知也 - Knowing is knowing, not knowing is not knowing; that is knowing.",
            "무지의 자각은 지혜의 시작이다 - Awareness of ignorance is the beginning of wisdom.",
            "Empty your mind, be formless, shapeless — like water.",
        ]
        
        quote = random.choice(quotes)
        print("\n💭 " + "─" * 60)
        self.animate_text(f"   {quote}", 0.02)
        print("─" * 63)
        
    def paradox_simulator(self):
        """Simulate the knowledge paradox"""
        print("\n" + "═" * 60)
        print("🌀 KNOWLEDGE PARADOX SIMULATOR 🌀")
        print("═" * 60)
        
        statements = [
            ("내가 아무것도 모른다는 것을 안다", "I know that I know nothing"),
            ("아는 것이 없음을 아는 것은 아는 것이다", "Knowing nothing is knowing something"),
            ("무지는 지혜의 첫걸음이다", "Ignorance is the first step to wisdom"),
            ("질문은 답보다 중요하다", "Questions are more important than answers"),
        ]
        
        for korean, english in statements:
            print(f"\n▶ {korean}")
            print(f"  ({english})")
            time.sleep(1)
            print("  🔄 Processing paradox...", end="", flush=True)
            time.sleep(0.5)
            print(" ✨ Mind expanded!")
            self.wisdom_level += 1
            
    def interactive_questions(self):
        """Interactive philosophical questions"""
        print("\n" + "═" * 60)
        print("❓ PHILOSOPHICAL INQUIRY ❓")
        print("═" * 60)
        
        questions = [
            {
                "question": "당신은 무엇을 알고 있습니까?\n(What do you know?)",
                "responses": [
                    "아무것도 모른다고 답했군요. 당신은 소크라테스와 같은 지혜를 가졌습니다!",
                    "Something? Then you must know that there's infinitely more you don't know!",
                    "Everything? The wise person knows they know nothing. Keep exploring!",
                ]
            },
            {
                "question": "무지를 인정하는 것이 왜 중요할까요?\n(Why is admitting ignorance important?)",
                "responses": [
                    "그렇죠! 무지의 인정은 배움의 시작입니다.",
                    "Indeed! Only by acknowledging what we don't know can we begin to learn.",
                    "Exactly! Humility opens the door to wisdom.",
                ]
            },
            {
                "question": "아무것도 모른다면, 어떻게 그 사실을 알 수 있나요?\n(If you know nothing, how do you know that?)",
                "responses": [
                    "훌륭한 질문입니다! 이것이 바로 지식의 역설입니다! 🤯",
                    "Brilliant! You've discovered the paradox at the heart of all knowledge! 🌟",
                    "This is the essence of philosophical inquiry! 🧠",
                ]
            }
        ]
        
        for i, q in enumerate(questions, 1):
            print(f"\n질문 {i}: {q['question']}")
            input("\n➤ 당신의 생각을 입력하세요 (Press Enter to continue): ")
            response = random.choice(q['responses'])
            self.animate_text(f"\n💡 {response}", 0.02)
            self.questions_asked += 1
            time.sleep(1)
            
    def knowledge_meter(self):
        """Display a visual representation of the knowledge paradox"""
        print("\n" + "═" * 60)
        print("📊 KNOWLEDGE PARADOX METER 📊")
        print("═" * 60)
        
        # As you gain wisdom, you realize how much you don't know
        known = min(self.wisdom_level * 10, 100)
        unknown = 100 - (known // 2)  # The more you know, the more you realize you don't know
        
        print(f"\n당신이 아는 것 (What you know):")
        print(f"[{'█' * (known // 10)}{'░' * (10 - known // 10)}] {known}%")
        
        print(f"\n당신이 모르는 것을 아는 것 (Awareness of what you don't know):")
        print(f"[{'█' * (unknown // 10)}{'░' * (10 - unknown // 10)}] {unknown}%")
        
        print(f"\n지혜 레벨 (Wisdom Level): {self.wisdom_level} ⭐")
        print(f"묻은 질문들 (Questions Asked): {self.questions_asked} ❓")
        
        if self.wisdom_level >= 3:
            print("\n🎓 축하합니다! 당신은 진정한 철학자입니다!")
            print("   (Congratulations! You are a true philosopher!)")
        
    def meditation_mode(self):
        """A moment of reflection"""
        print("\n" + "═" * 60)
        print("🧘 MEDITATION MODE 🧘")
        print("═" * 60)
        print("\n잠시 멈추고 생각해봅시다...")
        print("(Let's pause and reflect...)\n")
        
        meditations = [
            "빈 잔만이 물을 담을 수 있다",
            "Empty your cup so that it may be filled",
            "모르는 것을 아는 자는 겸손하다",
            "The one who knows they don't know is humble",
            "질문하는 것을 두려워하지 마라",
            "Don't be afraid to ask questions",
        ]
        
        for meditation in meditations:
            print(f"   ✨ {meditation}")
            time.sleep(1.5)
            
        print("\n🌸 마음이 평화로워졌습니다... (Mind at peace...)")
        
    def run(self):
        """Run the complete philosophical journey"""
        self.display_ascii_art()
        time.sleep(2)
        
        self.display_philosophical_quotes()
        time.sleep(2)
        
        self.paradox_simulator()
        time.sleep(2)
        
        self.interactive_questions()
        time.sleep(1)
        
        self.meditation_mode()
        time.sleep(2)
        
        self.knowledge_meter()
        
        print("\n" + "═" * 60)
        self.animate_text("✨ 철학적 여정이 완료되었습니다! (Philosophical journey complete!)", 0.03)
        print("═" * 60)
        print("\n기억하세요: 나는 아무것도 모른다... 그리고 그것이 괜찮습니다! 💫")
        print("Remember: I know nothing... and that's okay! 💫\n")


def main():
    """Main entry point"""
    print("\n🌟 철학적 여정을 시작합니다... (Starting philosophical journey...)\n")
    time.sleep(1)
    
    journey = KnowledgeParadox()
    
    try:
        journey.run()
    except KeyboardInterrupt:
        print("\n\n⚠️  여정이 중단되었습니다. (Journey interrupted.)")
        print("하지만 기억하세요: 멈추는 것도 배움입니다! 🌟\n")
    
    print("─" * 60)
    print("프로그램을 만들어준 것에 감사합니다! (Thank you for running this program!)")
    print("─" * 60 + "\n")


if __name__ == "__main__":
    main()
