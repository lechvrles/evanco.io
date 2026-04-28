#bot = Client("241963676:6To81nm5jA6rC4o0HyGw4zVu0sQqB8m9HGQ")

from balethon import Client
from balethon.conditions import private
from balethon.objects import InlineKeyboard, File

bot = Client("241963676:6To81nm5jA6rC4o0HyGw4zVu0sQqB8m9HGQ")

#main func
@bot.on_message(private)
async def answer_message(message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="به ربات رسمی اِوان خوش آمدید",
        reply_markup=InlineKeyboard(
            [("راهنمای نصب","install")],
            [("پشتیبانی","support")]
        )
    )

#main buttons
@bot.on_callback_query()
async def answer_callback_query(callback_query):
    if callback_query.data == "install":                                                   #راهنمای نصب 
        await callback_query.message.edit_text(
            "برای دریافت فایل های راهنما یکی از گزینه های زیر را انتخاب کنید",
            InlineKeyboard(
                [("ست کردن ریموت ها","pdf1")],
                [("فرم اجرا زیرساخت","pdf2")],
                [("نصب نرم افزار و طریقه اتصال به پنل","pdf3")],
                [("بازگشت","main")]
            )
        )            
        await callback_query.answer()

    elif callback_query.data == "support":                                                  #پشتیبانی
        await callback_query.message.edit_text(
           "برای دریافت مشاوره، ثبت سفارش یا هرگونه سوال، با ما در ارتباط باشید."\
           "\n.ما همیشه پاسخگوی شما هستیم",
            InlineKeyboard(
                [("تماس با ما","call")],
                [("سوالات متداول","faqs")],
                [("بازگشت","main")]
            )
        )

#dep buttons
    elif callback_query.data == "call":                                         #بخش تماس با ما زیر مجومه پشتیبانی
        await callback_query.message.edit_text(
            "*راه های تماس با ما*\n"\
            "\n*وبسایت*: www.evantechco.ir\n\n*ایمیل*: info@evantechco.com\n\n*تلفن پشتیبانی*: +۹۸۵۱۳۳۸۹۶۴۶۰\nروزهای شنبه تا چهارشنبه از ساعت ۹ صبح الی ۱۴"\
            "\n\nکانال *بله*: https://ble.ir/evantechco\n\n*نشانی ما*: مشهد، سیدی، بلوار شهید اصلانی، خیابان خلج،مقابل خلج یک، مجتمع مرکز توسعه پژوهشگاه وزارت نیرو، طبقه دوم، واحد ۲۱۱",
            InlineKeyboard(
                [("بازگشت به منو پشتیبانی","support")],
                [("بازگشت به منو اصلی","main")]
            )
        )    

    elif callback_query.data == "faqs":                                        #بخش سوالات متداول زیر مجموعه پشتیبانی
        await callback_query.message.edit_text(
            "*آیا امکان شخصی‌سازی سیستم‌های هوشمند برای هر پروژه وجود دارد؟*\nبله، تمامی محصولات و راهکارهای ما قابل تنظیم بر اساس نیاز و نقشه‌ی هر پروژه هستند. تیم ما با بررسی دقیق فضا، بهترین طراحی را متناسب با سبک معماری و نیازهای شما ارائه می‌دهد.\n\n"\
            "*پشتیبانی و خدمات پس از فروش شما به چه صورت است؟*\n"\
            "ما خدمات پشتیبانی فنی و آموزش کامل استفاده از سیستم‌ها را ارائه می‌دهیم. همچنین در صورت بروز مشکل یا نیاز به توسعه سیستم، تیم فنی ما در سریع‌ترین زمان ممکن در دسترس خواهد بود.",
            InlineKeyboard(
                [("بازگشت به منو پشتیبانی","support")],
                [("بازگشت به منو اصلی","main")]
            )
        )

#back to main
    elif callback_query.data == "main":
          await answer_message(callback_query.message) 
          await callback_query.answer()
            
#PATH/File
    elif callback_query.data == "pdf1":
        await bot.send_document(
            chat_id=callback_query.message.chat.id,
            document=File("https://storage.iran.liara.space/zarin1/v1/2026-04-27/23149e8ac33c9dd3646df52e7e31891b.pdf"),
            caption="ست کردن ریموت ها"
        )
    elif callback_query.data == "pdf2":
        await bot.send_document(
            chat_id=callback_query.message.chat.id,
            document=File("https://storage.iran.liara.space/zarin1/v1/2026-04-27/0bab7d17e6fbe7b51257729a81248e3b.pdf"),
            caption="فرم اجرا زیرساخت"
        )
    elif callback_query.data == "pdf3":
        await bot.send_document(
            chat_id=callback_query.message.chat.id,
            document=File("https://storage.iran.liara.space/zarin1/v1/2026-04-27/0fb7b53247de6679fefca0737c4c8de2.pdf"),
            caption="نصب نرم افزار و طریقه اتصال به پنل"
        )
        await callback_query.answer("با موفقیت ارسال شد")

bot.run()








