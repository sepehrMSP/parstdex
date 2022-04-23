from parstdex import Parstdex, settings
import pprint
from parstdex.utils.datatime_extractor import extract_duration

tests = [
    "از امروز تا فردا",
    "از سه شنبه هفته قبل  لغایت ۳ فروردین ",
    "از سال بعد هر روز درس می‌خوانم",
    "هر سه‌شنبه",
    "دو شنبه ها راس ساعت ۵ عصر",
    "دوشنبه شب تولد حاج آقا است",
    "تا دو روز دیگر",
    "در محل همایش های بین المللی مورخ هفدهم فروردین  سال هزار و پانصد ونود و سه",
    "تمام پنج شنبه های سال",
    " در تاریخ ۱۳۹۸/۰۳/۱۴ ایران موفق به بازگشایی شدیم",
    "از چهار سال پیش تا به حال سمت آن نرفتم",
    "دیروز به حمام رفتم",
    "از پریشب تا دیشب تمام مدت خواب به چشمانم نیامده",
    # "همیشه",
    "همین چهارشنبه",
    "سه‌شنبه سه هفته قبل",
    "این اتفاق سه روز بعد از اولین چهارشنبه‌ی سال رخ داد",
    "در ۲۲ بهمن چهار سال پیش انقلاب شد",
    "از امروز تا پایان هفته آتی وقت مهلت ارسال درخواست ها میباشد",
    "ماه آینده",
    "طی این ماه",
    "۳۰ روز گذشته",
    "در بازه ۱ ماهه درس میخوانم",
    "در فاصله دو هفته قرار است به سرانجام برسیم",
    "در طول ۱ سال پروژه را انجام دادم",
    "در مدت ۹ ماه زایمان کردم",
    "ظرف دو روز تمرین را انجام میدهم",
    "از ۲۰ روز پیش تا کنون در گیر آن بودیم",
    "هزاره سوم",
    "دو قرن سکوت ایرانیان",
    "بین اسفند و فروردین سال ۵۷ جنگ بود",
    "در عرض ۱ ثانیه ازین رو به آن رو شد",
    "بعد از تصادف دیگر هر یکشنبه به کلیسا میروم",
    "سال ها درس خواندم",
]



model = Parstdex(debug_mode=False)


def run():
    result = {}
    for sentence in tests:
        # spans = model.extract_span(sentence)
        # result['spans'] = spans

        print(sentence)

        markers = model.extract_marker(sentence)
        result['markers'] = markers

        values = model.extract_value(sentence)
        # a =  extract_duration(markers=markers, values=values)
        # print(a)
        result['values'] = values

        # ners = model.extract_ner(sentence)
        # result['ner'] = ners

        pprint.pprint(result,)
        print("==" * 50)


run()
