
import asyncio







async def Login_to(page):
    try:
        acct_balance = await page.waitForSelector('span[id="j_balance"]', timeout=10000)
        spt_acct_balance = int((await (await acct_balance.getProperty('textContent')).jsonValue()).strip().replace('NGN ','').replace(',','').split('.')[0])
        if spt_acct_balance:
            print(f"\n>>> ALREADY LOGGED IN! ACCOUNT BALANCE: {spt_acct_balance} <<<\n")
            return False
    except:
        pass
    
    print("\n>>> NOT LOGGED IN! PROCEEDING TO LOGIN... <<<\n")
    email_to_input = input("Enter phone number:::::::: ")
    password_to_input = input("Enter password:::::::: ")

    email_to = await page.waitForSelector('div.m-phone input[name="phone"]', timeout=7000)
    await page.evaluate('(el) => el.scrollIntoView({ behavior: "smooth", block: "center" })', email_to)
    await email_to.click()
    await asyncio.sleep(1)
    await email_to.click()
    await asyncio.sleep(1)
    await page.keyboard.down('Control')
    await page.keyboard.press('A')
    await page.keyboard.up('Control')
    await page.keyboard.press('Backspace')
    await asyncio.sleep(1)
 
    # 3️⃣ Type the new stake
    await email_to.type(str(email_to_input))
    await asyncio.sleep(1)


    password_to = await page.waitForSelector('div.m-psd input[name="psd"]', timeout=4000)
    await page.evaluate('(el) => el.scrollIntoView({ behavior: "smooth", block: "center" })', password_to)
    await password_to.click()
    await asyncio.sleep(1)
    await password_to.click()
    await asyncio.sleep(1)
    await page.keyboard.down('Control')
    await page.keyboard.press('A')
    await page.keyboard.up('Control')
    await page.keyboard.press('Backspace')
    await asyncio.sleep(1)

    # 3️⃣ Type the new stake
    await password_to.type(str(password_to_input))   
    await asyncio.sleep(1)

    Login_to = await page.waitForSelector('button[name="logIn"]', timeout=4000)
    Login_to_click = await page.evaluate('(el) => el.scrollIntoView({ behavior: "smooth", block: "center" })', Login_to)
    await Login_to.click()
    await asyncio.sleep(.5)
    await Login_to.click()
    await asyncio.sleep(3)



    now_balance = await page.waitForSelector('span[id="j_balance"]', timeout=15000)
    try:
        spt_acct_balance = int((await (await now_balance.getProperty('textContent')).jsonValue()).strip().replace('NGN ','').replace(',','').split('.')[0])
    except:
        spt_acct_balance = None
    if spt_acct_balance:
        print(f"\n>>> ALREADY LOGGED IN! ACCOUNT BALANCE: {spt_acct_balance} <<<\n")
    else:
        input("PRESS ENTER AFTER LOGGING IN AND SETTING UP THE PAGE TO AUTOMATE...")