from balethon import Client
from balethon.conditions import private, is_joined
from balethon.objects import InlineKeyboard, File, InlineKeyboardButton

<<<<<<< HEAD
bot = Client("TOKEN")
channel_button = InlineKeyboardButton("کانال اِوان", url="https://ble.ir/evantechco")
CHAT_ID = 4780203817


#                                                                                          <-----main func----->

@bot.on_message(~is_joined(CHAT_ID))
async def not_joined(message):
    await message.reply("برای دسترسی به بازو ابتدا عضو کانال بله ما شوید")

@bot.on_message(private)
async def answer_message(message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="سلام!👋\nبه بازوی رسمی اِوان خوش آمدید\n\nبرای استفاده از خدمات بازو، لطفا یکی از دکمه های زیر را انتخاب کنید ⬇️",
        reply_markup=InlineKeyboard(
            [("راهنمای نصب","install"),
            ("پشتیبانی","support")],
            [("کاتالوگ اِوان","catalog")],
            [channel_button]
        )
    )
    await bot.set_webhook("https://bot.evanteco.com/evanbot/main.py")
    

#                                                                                        <-----main buttons----->
@bot.on_callback_query(private)
async def answer_callback_query(callback_query):

    if callback_query.data == "install":                                                        #راهنمای نصب 
        await callback_query.message.edit_text(
            "برای دریافت فایل های راهنما یکی از گزینه های زیر را انتخاب کنید",
            InlineKeyboard(
                [("ست کردن ریموت ها","pdf1"),
                ("فرم اجرا زیرساخت","pdf2")],
                [("نصب نرم افزار و طریقه اتصال به پنل","pdf3")],
                [("بازگشت","main")]
            )
        )            
        await callback_query.answer()

    elif callback_query.data == "support":                                                        #پشتیبانی
        await callback_query.message.edit_text(
           "برای دریافت مشاوره، ثبت سفارش یا هرگونه سوال، با ما در ارتباط باشید."\
           "\n.ما همیشه پاسخگوی شما هستیم",
            InlineKeyboard(
                [("سوالات متداول","faqs"),
                ("تماس با ما","call")],
                [("بازگشت","main")]
            )
        )

#                                                                                     <-------dep buttons------>

    elif callback_query.data == "call":                                              #بخش تماس با ما زیر مجومه پشتیبانی
        await callback_query.message.edit_text(
            "*راه های تماس با ما*\n"\
            "\n*وبسایت*: www.evantechco.ir\n\n*ایمیل*: info@evantechco.com\n\n*تلفن پشتیبانی*: +۹۸۵۱۳۳۸۹۶۴۶۰\nروزهای شنبه تا چهارشنبه از ساعت ۹ صبح الی ۱۴"\
            "\n\nکانال *بله*: https://ble.ir/evantechco\n\n*نشانی ما*: مشهد، سیدی، بلوار شهید اصلانی، خیابان خلج، مقابل خلج یک، مجتمع مرکز توسعه پژوهشگاه وزارت نیرو، طبقه دوم، واحد ۲۱۱",
            InlineKeyboard(
                [("بازگشت","support")],
                [("منو اصلی","main")]
            )
        )    

    elif callback_query.data == "faqs":                                              #بخش سوالات متداول زیر مجموعه پشتیبانی
        await callback_query.message.edit_text(
            "به بخش *پرسش های متداول تعاملی* خوش آمدید\nبا استفاده از دکمه های زیر به متداول ترین پرسش های شما کاربران عزیز پاسخ داده شده است. چنانچه نیاز به کمک بیشتر دارید از طریق بخش *تماس با ما*، با پشتیبان های ما در ارتباط باشید.",
            InlineKeyboard(
                [("اطلاعات بیشتر در مورد هوشمندسازی","q1")],
                [("مزایای هوشمندسازی","q2")],
                [("مراحل هوشمندسازی","q3")],
                [("هوشمندسازی با اِوان","q4")],
                [("منوی اصلی","main"),("بازگشت","support")]
            )
        )


    elif callback_query.data == "q1":                                                    #اطلاعات بیشتر در مورد هوشمندسازی
        await callback_query.message.edit_text(
            "لطفا یکی از گزینه های زیر را انتخاب کنید.",
            InlineKeyboard(
                [("تفاوت ساختمان هوشمند و معمولی چیست؟","q12")],
                [("آیا هزینه هوشمندسازی خانه گران است؟","q13")],
                [("امنیت خانه های هوشمند چگونه است؟","q15")],
                [("آیا هوشمندسازی فقط برای خانه‌های لوکس و پرهزینه است؟","q16")],
                [("آیا امکان هوشمندسازی فقط برای بخش‌های خاصی از خانه وجود دارد؟","q18")],
                [("در صورت قطع شدن اینترنت، عملکرد خانه هوشمند چگونه خواهد بود؟","q19")],
                [("بازگشت","faqs")]
            )
        )   
    elif callback_query.data == "q12":
        await callback_query.message.edit_text(
            "*تفاوت ساختمان هوشمند و معمولی چیست؟*\n\n"\
            "تفاوت اصلی ساختمان هوشمند و معمولی در سطح کنترل و اتوماسیون است. در ساختمان هوشمند، تجهیزات مختلف مانند روشنایی، گرمایش، امنیت و لوازم خانگی به‌صورت خودکار یا از راه دور از طریق اپلیکیشن یا فرمان صوتی کنترل می‌شوند." \
            "اما در ساختمان معمولی، این کنترل‌ها دستی و سنتی هستند. ساختمان هوشمند امنیت، راحتی و بهره‌وری انرژی بیشتری ارائه می‌دهد، در حالی که ساختمان های معمولی فاقد این امکانات هوشمند هستند.",
            InlineKeyboard([("بازگشت","q1")])
        ) 
    elif callback_query.data == "q13":
        await callback_query.message.edit_text(
            "*آیا هزینه هوشمندسازی خانه گران است؟*\n\n"\
            "هزینه خانه های هوشمند بر حسب تعداد، برند و نوع تجهیزات هوشمندسازی، خواسته‌های ساکنین خانه و غیره متغیر است. به علاوه امکان به حداقل رساندن هزینه هوشمندسازی با نصب تجهیزات هوشمند ارزان قیمت نیز وجود دارد.",
            InlineKeyboard([("بازگشت","q1")])
        ) 
    elif callback_query.data == "q15":
        await callback_query.message.edit_text(
            "*امنیت خانه های هوشمند چگونه است؟*\n\n"\
            "بزرگترین تهدید تکنولوژی‌های دیجیتال، هک و نفوذ به سیستم‌های آنهاست. این مورد در خانه‌ های هوشمند نیز صدق می‌کند. اما هرساله و با توجه به اهمیت موضوع، شرکت‌های تولید کننده تجهیزات هوشمند،" \
            "اقدام به بروزرسانی و افزایش امنیت کدهای خود کرده و همواره راه‌های نفوذ به این سیستم‌ها را سخت‌تر می‌کنند. به طور کلی سیستم‌های هوشمند از امنیت به مراتب بیشتری نسبت به سامانه‌های قدیمی و غیرهوشمند برخوردارند.",
            InlineKeyboard([("بازگشت","q1")])
        )         
    elif callback_query.data == "q16":
        await callback_query.message.edit_text(
            "*آیا هوشمندسازی فقط برای خانه‌های لوکس و پرهزینه است؟*\n\n"\
            "خیر. زیبایی فناوری هوشمند در انعطاف‌پذیری آن است. شما می‌توانید با یک پکیج پایه هوشمندسازی خانه (مانند کنترل روشنایی و سرمایش/گرمایش) شروع کرده و در آینده سیستم را گسترش دهید.",
            InlineKeyboard([("بازگشت","q1")])
        ) 
    elif callback_query.data == "q18":
        await callback_query.message.edit_text(
            "*آیا امکان هوشمندسازی فقط برای بخش‌های خاصی از خانه (مثلاً فقط پذیرایی) وجود دارد؟*\n\n"\
            "بله، یکی از مزایای سیستم‌های هوشمند اِوان، قابلیت اجرای ماژولار یا مرحله‌ای است. شما الزامی به هوشمندسازی کل ساختمان ندارید و می‌توانید تنها با هوشمند کردن سیستم روشنایی یا سیستم سرمایش/گرمایش شروع کنید." \
            "این ویژگی به شما اجازه می‌دهد متناسب با بودجه خود، به مرور زمان تجهیزات جدیدی را به شبکه هوشمند خانه اضافه کنید.",
            InlineKeyboard([("بازگشت","q1")])
        ) 
    elif callback_query.data == "q19":
        await callback_query.message.edit_text(
            "*در صورت قطع شدن اینترنت، عملکرد خانه هوشمند چگونه خواهد بود؟*\n\n"\
            "در اکثر پروتکل‌های استاندارد (به ویژه پروتکل‌های سیمی مانند KNX و Modbus یا بی‌سیم مانند WiFi , NRF و Zigbee)، کنترل داخلی خانه (مانند کلیدهای روشنایی و سنسورها) بدون نیاز به اینترنت و در بستر شبکه داخلی برقرار است. اینترنت تنها برای کنترل از راه دور (خارج از منزل) و دریافت برخی آپدیت‌ها مورد نیاز است؛ بنابراین در صورت قطع اینترنت، زندگی روزمره شما در خانه مختل نمی‌شود.",
            InlineKeyboard(
                [("بازگشت","q1")]
            )
        ) 

    elif callback_query.data == "q2":                                                         #مزایای هوشمندسازی
        await callback_query.message.edit_text(
            "*خانه هوشمند چگونه به کاهش هزینه‌های انرژی کمک می‌کند؟*\n\n"\
            "از طریق سیستم‌هایی مانند ترموستات هوشمند که الگوی رفت‌وآمد شما را یاد گرفته و دمای فضاهای خالی را تنظیم می‌کند، و همچنین کنترل هوشمند روشنایی که از روشن ماندن بی‌دلیل چراغ‌ها جلوگیری می‌کند.",
            InlineKeyboard([("بازگشت","faqs")])
        )

    elif callback_query.data =="q3":                                                          #مراحل هوشمندسازی
        await callback_query.message.edit_text(
            "لطفا یکی از گزینه های زیر را انتخاب کنید.",
            InlineKeyboard(
                [("در چه مرحله‌ای باید برای خانه هوشمند اقدام کنیم؟","q31")],
                [("چگونه خانه خود را هوشمند کنیم؟","q34")],
                [("بازگشت","faqs")]
            )
        )
    elif callback_query.data == "q31":
        await callback_query.message.edit_text(
            "*در چه مرحله‌ای باید برای خانه هوشمند اقدام کنیم؟*\n\n"\
            "از آنجایی که سیم کشی ‌خانه‌ی هوشمند با معمولی تفاوت دارد، باید در زمان ترسیم نقشه برق خانه بسترهای مورد نیاز برای هوشمند سازی نیز تعبیه شود. برای خانه‌هایی که بستر و سیم کشی مورد نیاز برای هوشمند سازی را ندارند نیز می‌توانیم از تجهیزات وایرلس استفاده کنیم.",
            InlineKeyboard([("بازگشت","q3")])
        )
    elif callback_query.data == "q34":
        await callback_query.message.edit_text(
            "*چگونه خانه خود را هوشمند کنیم؟*\n\n"\
            "ایجاد خانه هوشمند شامل مراحلی مانند برنامه‌ریزی اولیه برای تعیین نیازها، انتخاب و خرید تجهیزات مناسب، نصب و راه‌اندازی صحیح، پیکربندی و آزمایش سیستم‌ها و در نهایت آموزش ساکنان برای استفاده بهینه از امکانات هوشمند است تا هماهنگی و یکپارچگی مؤثری بین تجهیزات برقرار شود.",
            InlineKeyboard([("بازگشت","q3")])
        )    

    elif callback_query.data == "q4":                                                        #هوشمندسازی با اِوان
        await callback_query.message.edit_text(
            "لطفا یکی از گزینه های زیر را انتخاب کنید.",
            InlineKeyboard(
                [("خدمات پس از فروش و پشتیبانی تجهیزات هوشمند اِوان شامل چه مواردی است؟","q410")],
                [("آیا امکان شخصی‌سازی سیستم‌های هوشمند برای هر پروژه وجود دارد؟","q411")],
                [("پشتیبانی و خدمات پس از فروش شما به چه صورت است؟","q412")],
                [("بازگشت","faqs")]
            )
        )
    elif callback_query.data == "q410":
        await callback_query.message.edit_text(
            "*پشتیبانی تجهیزات هوشمند اِوان شامل چه مواردی است؟*\n\n"\
            "شرکت اِوان با سالها سابقه، پایداری سیستم‌های نصب شده را تضمین می‌کند. خدمات ما شامل گارانتی تعویض قطعات، پشتیبانی فنی برای رفع ایرادات احتمالی نرم‌افزاری و سخت‌افزاری، و همچنین به‌روزرسانی اپلیکیشن‌ها است. از آنجایی که ما از پروتکل‌های استاندارد جهانی استفاده می‌کنیم، خیالتان از بابت تامین قطعات و توسعه سیستم در سال‌های آینده کاملا آسوده خواهد بود.",
            InlineKeyboard([("بازگشت","q4")])
        )    
    elif callback_query.data == "q411":
        await callback_query.message.edit_text(
            "*آیا امکان شخصی‌سازی سیستم‌های هوشمند برای هر پروژه وجود دارد؟*\n\n"\
            "بله، تمامی محصولات و راهکارهای ما قابل تنظیم بر اساس نیاز و نقشه‌ی هر پروژه هستند. تیم ما با بررسی دقیق فضا، بهترین طراحی را متناسب با سبک معماری و نیازهای شما ارائه می‌دهد.",
            InlineKeyboard([("بازگشت","q4")])
        )    
    elif callback_query.data == "q412":
        await callback_query.message.edit_text(
            "*پشتیبانی و خدمات پس از فروش شما به چه صورت است؟*\n\n"\
            "تمامی محصولات ما ۳ سال گارانتی و ۱۰ سال خدمات پس از فروش همراه پشتیبانی فنی و آموزش کامل استفاده از سیستم‌ها را دارند. همچنین در صورت بروز مشکل یا نیاز به توسعه سیستم، تیم فنی ما در سریع‌ترین زمان ممکن در دسترس خواهد بود.",
            InlineKeyboard([("بازگشت","q4")])
        )

#                                                                                     <-------back buttons------>
    elif callback_query.data == "main":
          await answer_message(callback_query.message) 
          await callback_query.answer()
          
#PATH/File
    elif callback_query.data == "pdf1":
        await bot.send_document(
            chat_id=callback_query.message.chat.id,
            document=File("https://evancloud.s3.ir-thr-at1.arvanstorage.ir/%D8%B3%D8%AA%20%DA%A9%D8%B1%D8%AF%D9%86%20%D8%B1%DB%8C%D9%85%D9%88%D8%AA%20%D9%87%D8%A7.pdf?versionId="),
            #caption="ست کردن ریموت ها"
        )
    elif callback_query.data == "pdf2":
        await bot.send_document(
            chat_id=callback_query.message.chat.id,
            document=File("https://evancloud.s3.ir-thr-at1.arvanstorage.ir/%D9%81%D8%B1%D9%85%20%D8%A7%D8%AC%D8%B1%D8%A7%20%D8%B2%DB%8C%D8%B1%20%D8%B3%D8%A7%D8%AE%D8%AA.pdf?versionId="),
            #caption="فرم اجرا زیرساخت"
        )
    elif callback_query.data == "pdf3":
        await bot.send_document(
            chat_id=callback_query.message.chat.id,
            document=File("https://evancloud.s3.ir-thr-at1.arvanstorage.ir/%D9%86%D8%B5%D8%A8%20%D9%86%D8%B1%D9%85%20%D8%A7%D9%81%D8%B2%D8%A7%D8%B1%20%D9%88%20%D8%B7%D8%B1%DB%8C%D9%82%D9%87%20%D8%A7%D8%AA%D8%B5%D8%A7%D9%84%20%D8%A8%D9%87%20%D9%BE%D9%86%D9%84.pdf?versionId="),
            #caption="نصب نرم افزار و طریقه اتصال به پنل"
        )
    elif callback_query.data == "catalog":
        await bot.send_document(
            chat_id=callback_query.message.chat.id,
            document=File("https://evancloud.s3.ir-thr-at1.arvanstorage.ir/%DA%A9%D8%A7%D8%AA%D8%A7%D9%84%D9%88%DA%AF%20%D8%A7%D9%90%D9%88%D8%A7%D9%86.pdf?versionId=")
        )
        await callback_query.answer("با موفقیت ارسال شد")

bot.run()