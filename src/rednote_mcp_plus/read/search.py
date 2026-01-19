import re
from typing import List
from playwright.async_api import async_playwright
import asyncio


async def search(keyWord: str) -> str:
    """
    搜索小红书笔记
    :param keyWord: 搜索关键词
    """
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(storage_state="src/rednote_mcp_plus/cookie/rednote_cookies.json")
        page = await context.new_page()
        await page.goto("https://www.xiaohongshu.com/explore")
        print("🌐 导航到小红书主页...")
        await page.wait_for_timeout(10000)
        login_button = page.locator("form").get_by_role("button", name="登录")
        if(await login_button.is_visible()):
            return "❌ 未登录小红书，请先登录"
        
        await page.get_by_role("textbox", name="搜索小红书").fill(keyWord)
        await page.locator(".search-icon").click()
        
        try:
            # 无限等待，直到页面被关闭
            await page.wait_for_event("close", timeout=0)
        except Exception as e:
            print(f"等待过程中断: {e}")
        finally:
            await browser.close()
            await context.close()
            
        return "✅ 搜索操作完成"
            
        

if __name__ == "__main__":
    result = asyncio.run(search("测试"))
    print(result)