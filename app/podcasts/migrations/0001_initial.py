# Generated by Django 4.0.2 on 2022-08-19 17:39

import uuid

import podcasts.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Episode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("file", models.FileField(upload_to="")),
                ("file_length", models.IntegerField()),
                (
                    "file_type",
                    models.CharField(
                        choices=[
                            ("audio/x-m4a", "audio/x-m4a"),
                            ("audio/mpeg", "audio/mpeg"),
                            ("video/quicktime", "video/quicktime"),
                            ("video/mp4", "video/mp4"),
                            ("video/x-m4v", "video/x-m4v"),
                            ("application/pdf", "application/pdf"),
                        ],
                        max_length=20,
                    ),
                ),
                ("guid", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("published_date", models.DateTimeField()),
                ("description", models.TextField(max_length=3000)),
                ("link", models.URLField()),
                ("duration", models.IntegerField()),
                ("image", models.ImageField(upload_to="")),
                (
                    "explicit",
                    models.CharField(
                        choices=[("True", "True"), ("False", "False")], max_length=5
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Show",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("description", models.TextField(max_length=3000)),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("aa", "Afar"),
                            ("ab", "Abkhazian"),
                            ("af", "Afrikaans"),
                            ("ak", "Akan"),
                            ("am", "Amharic"),
                            ("ar", "Arabic"),
                            ("an", "Aragonese"),
                            ("as", "Assamese"),
                            ("av", "Avaric"),
                            ("ae", "Avestan"),
                            ("ay", "Aymara"),
                            ("az", "Azerbaijani"),
                            ("ba", "Bashkir"),
                            ("bm", "Bambara"),
                            ("be", "Belarusian"),
                            ("bn", "Bengali"),
                            ("bh", "Bihari languages"),
                            ("bi", "Bislama"),
                            ("bs", "Bosnian"),
                            ("br", "Breton"),
                            ("bg", "Bulgarian"),
                            ("ca", "Catalan; Valencian"),
                            ("ch", "Chamorro"),
                            ("ce", "Chechen"),
                            (
                                "cu",
                                "Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic",
                            ),
                            ("cv", "Chuvash"),
                            ("kw", "Cornish"),
                            ("co", "Corsican"),
                            ("cr", "Cree"),
                            ("da", "Danish"),
                            ("dv", "Divehi; Dhivehi; Maldivian"),
                            ("dz", "Dzongkha"),
                            ("en", "English"),
                            ("eo", "Esperanto"),
                            ("et", "Estonian"),
                            ("ee", "Ewe"),
                            ("fo", "Faroese"),
                            ("fj", "Fijian"),
                            ("fi", "Finnish"),
                            ("fy", "Western Frisian"),
                            ("ff", "Fulah"),
                            ("gd", "Gaelic; Scottish Gaelic"),
                            ("ga", "Irish"),
                            ("gl", "Galician"),
                            ("gv", "Manx"),
                            ("gn", "Guarani"),
                            ("gu", "Gujarati"),
                            ("ht", "Haitian; Haitian Creole"),
                            ("ha", "Hausa"),
                            ("he", "Hebrew"),
                            ("hz", "Herero"),
                            ("hi", "Hindi"),
                            ("ho", "Hiri Motu"),
                            ("hr", "Croatian"),
                            ("hu", "Hungarian"),
                            ("ig", "Igbo"),
                            ("io", "Ido"),
                            ("ii", "Sichuan Yi; Nuosu"),
                            ("iu", "Inuktitut"),
                            ("ie", "Interlingue; Occidental"),
                            (
                                "ia",
                                "Interlingua (International Auxiliary Language Association)",
                            ),
                            ("id", "Indonesian"),
                            ("ik", "Inupiaq"),
                            ("it", "Italian"),
                            ("jv", "Javanese"),
                            ("ja", "Japanese"),
                            ("kl", "Kalaallisut; Greenlandic"),
                            ("kn", "Kannada"),
                            ("ks", "Kashmiri"),
                            ("kr", "Kanuri"),
                            ("kk", "Kazakh"),
                            ("km", "Central Khmer"),
                            ("ki", "Kikuyu; Gikuyu"),
                            ("rw", "Kinyarwanda"),
                            ("ky", "Kirghiz; Kyrgyz"),
                            ("kv", "Komi"),
                            ("kg", "Kongo"),
                            ("ko", "Korean"),
                            ("kj", "Kuanyama; Kwanyama"),
                            ("ku", "Kurdish"),
                            ("lo", "Lao"),
                            ("la", "Latin"),
                            ("lv", "Latvian"),
                            ("li", "Limburgan; Limburger; Limburgish"),
                            ("ln", "Lingala"),
                            ("lt", "Lithuanian"),
                            ("lb", "Luxembourgish; Letzeburgesch"),
                            ("lu", "Luba-Katanga"),
                            ("lg", "Ganda"),
                            ("mh", "Marshallese"),
                            ("ml", "Malayalam"),
                            ("mr", "Marathi"),
                            ("mg", "Malagasy"),
                            ("mt", "Maltese"),
                            ("mn", "Mongolian"),
                            ("na", "Nauru"),
                            ("nv", "Navajo; Navaho"),
                            ("nr", "Ndebele, South; South Ndebele"),
                            ("nd", "Ndebele, North; North Ndebele"),
                            ("ng", "Ndonga"),
                            ("ne", "Nepali"),
                            ("nn", "Norwegian Nynorsk; Nynorsk, Norwegian"),
                            ("nb", "Bokmål, Norwegian; Norwegian Bokmål"),
                            ("no", "Norwegian"),
                            ("ny", "Chichewa; Chewa; Nyanja"),
                            ("oc", "Occitan (post 1500)"),
                            ("oj", "Ojibwa"),
                            ("or", "Oriya"),
                            ("om", "Oromo"),
                            ("os", "Ossetian; Ossetic"),
                            ("pa", "Panjabi; Punjabi"),
                            ("pi", "Pali"),
                            ("pl", "Polish"),
                            ("pt", "Portuguese"),
                            ("ps", "Pushto; Pashto"),
                            ("qu", "Quechua"),
                            ("rm", "Romansh"),
                            ("rn", "Rundi"),
                            ("ru", "Russian"),
                            ("sg", "Sango"),
                            ("sa", "Sanskrit"),
                            ("si", "Sinhala; Sinhalese"),
                            ("sl", "Slovenian"),
                            ("se", "Northern Sami"),
                            ("sm", "Samoan"),
                            ("sn", "Shona"),
                            ("sd", "Sindhi"),
                            ("so", "Somali"),
                            ("st", "Sotho, Southern"),
                            ("es", "Spanish; Castilian"),
                            ("sc", "Sardinian"),
                            ("sr", "Serbian"),
                            ("ss", "Swati"),
                            ("su", "Sundanese"),
                            ("sw", "Swahili"),
                            ("sv", "Swedish"),
                            ("ty", "Tahitian"),
                            ("ta", "Tamil"),
                            ("tt", "Tatar"),
                            ("te", "Telugu"),
                            ("tg", "Tajik"),
                            ("tl", "Tagalog"),
                            ("th", "Thai"),
                            ("ti", "Tigrinya"),
                            ("to", "Tonga (Tonga Islands)"),
                            ("tn", "Tswana"),
                            ("ts", "Tsonga"),
                            ("tk", "Turkmen"),
                            ("tr", "Turkish"),
                            ("tw", "Twi"),
                            ("ug", "Uighur; Uyghur"),
                            ("uk", "Ukrainian"),
                            ("ur", "Urdu"),
                            ("uz", "Uzbek"),
                            ("ve", "Venda"),
                            ("vi", "Vietnamese"),
                            ("vo", "Volapük"),
                            ("wa", "Walloon"),
                            ("wo", "Wolof"),
                            ("xh", "Xhosa"),
                            ("yi", "Yiddish"),
                            ("yo", "Yoruba"),
                            ("za", "Zhuang; Chuang"),
                            ("zu", "Zulu"),
                        ],
                        max_length=5,
                    ),
                ),
                ("link", models.URLField()),
                ("copyright", models.CharField(max_length=128)),
                (
                    "image",
                    models.ImageField(
                        upload_to="",
                        validators=[
                            podcasts.utils.validate_show_art_is_optimally_sized
                        ],
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Arts", "Arts"),
                            ("Books", "Books"),
                            ("Design", "Design"),
                            ("Fashion &amp Beauty", "Fashion & Beauty"),
                            ("Food", "Food"),
                            ("Performing Arts", "Performing Arts"),
                            ("Visual Arts", "Visual Arts"),
                            ("Business", "Business"),
                            ("Careers", "Careers"),
                            ("Entrepreneurship", "Entrepreneurship"),
                            ("Investing", "Investing"),
                            ("Management", "Management"),
                            ("Marketing", "Marketing"),
                            ("Non-Profit", "Non-Profit"),
                            ("Comedy", "Comedy"),
                            ("Comedy Interviews", "Comedy Interviews"),
                            ("Improv", "Improv"),
                            ("Stand-Up", "Stand-Up"),
                            ("Education", "Education"),
                            ("Courses", "Courses"),
                            ("How To", "How To"),
                            ("Language Learning", "Language Learning"),
                            ("Self-Improvement", "Self-Improvement"),
                            ("Fiction", "Fiction"),
                            ("Comedy Fiction", "Comedy Fiction"),
                            ("Drama", "Drama"),
                            ("Science Fiction", "Science Fiction"),
                            ("Government", "Government"),
                            ("History", "History"),
                            ("Health &amp;amp; Fitness", "Health & Fitness"),
                            ("Alternative Health", "Alternative Health"),
                            ("Fitness", "Fitness"),
                            ("Medicine", "Medicine"),
                            ("Mental Health", "Mental Health"),
                            ("Nutrition", "Nutrition"),
                            ("Sexuality", "Sexuality"),
                            ("Kids &amp; Family", "Kids & Family"),
                            ("Education for Kids", "Education for Kids"),
                            ("Parenting", "Parenting"),
                            ("Pets &amp; Animals", "Pets & Animals"),
                            ("Stories for Kids", "Stories for Kids"),
                            ("Leisure", "Leisure"),
                            ("Animation &amp; Manga", "Animation & Manga"),
                            ("Automotive", "Automotive"),
                            ("Aviation", "Aviation"),
                            ("Crafts", "Crafts"),
                            ("Games", "Games"),
                            ("Hobbies", "Hobbies"),
                            ("Home &amp;  Garden", "Home & Garden"),
                            ("Video Games", "Video Games"),
                            ("Music", "Music"),
                            ("Music Commentary", "Music Commentary"),
                            ("Music History", "Music History"),
                            ("Music Interviews", "Music Interviews"),
                            ("News", "News"),
                            ("Business News", "Business News"),
                            ("Daily News", "Daily News"),
                            ("Entertainment News", "Entertainment News"),
                            ("News Commentary", "News Commentary"),
                            ("Politics", "Politics"),
                            ("Sports News", "Sports News"),
                            ("Tech News", "Tech News"),
                            ("Religion &amp; Spirituality", "Religion & Spirituality"),
                            ("Buddhism", "Buddhism"),
                            ("Christianity", "Christianity"),
                            ("Hinduism", "Hinduism"),
                            ("Islam", "Islam"),
                            ("Judaism", "Judaism"),
                            ("Religion", "Religion"),
                            ("Spirituality", "Spirituality&nbsp;"),
                            ("Science", "Science"),
                            ("Astronomy", "Astronomy"),
                            ("Chemistry", "Chemistry"),
                            ("Earth Sciences", "Earth Sciences"),
                            ("Life Sciences", "Life Sciences"),
                            ("Mathematics", "Mathematics"),
                            ("Natural Sciences", "Natural Sciences"),
                            ("Nature", "Nature"),
                            ("Physics", "Physics"),
                            ("Social Sciences", "Social Sciences"),
                            ("Society &amp;amp; Culture", "Society & Culture"),
                            ("Documentary", "Documentary"),
                            ("Personal Journals", "Personal Journals"),
                            ("Philosophy", "Philosophy"),
                            ("Places &amp;amp; Travel", "Places & Travel"),
                            ("Relationships", "Relationships"),
                            ("Sports", "Sports"),
                            ("Baseball", "Baseball"),
                            ("Basketball", "Basketball"),
                            ("Cricket", "Cricket"),
                            ("Fantasy Sports", "Fantasy Sports"),
                            ("Football", "Football"),
                            ("Golf", "Golf"),
                            ("Hockey", "Hockey"),
                            ("Rugby", "Rugby"),
                            ("Soccer", "Soccer"),
                            ("Swimming", "Swimming"),
                            ("Tennis", "Tennis"),
                            ("Volleyball", "Volleyball"),
                            ("Wilderness", "Wilderness"),
                            ("Wrestling", "Wrestling"),
                            ("Technology", "Technology"),
                            ("True Crime", "True Crime"),
                            ("TV &amp;amp; Film", "TV & Film"),
                            ("After Shows", "After Shows"),
                            ("Film History", "Film History"),
                            ("Film Interviews", "Film Interviews"),
                            ("Film Reviews", "Film Reviews"),
                            ("TV Reviews", "TV Reviews"),
                        ],
                        max_length=40,
                    ),
                ),
                ("explicit", models.BooleanField()),
                ("author", models.CharField(max_length=120)),
                ("owner_name", models.CharField(max_length=120)),
                ("owner_email", models.EmailField(max_length=254)),
                (
                    "block",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")], max_length=3
                    ),
                ),
                (
                    "complete",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")], max_length=3
                    ),
                ),
            ],
        ),
    ]
