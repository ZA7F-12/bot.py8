Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\shooq> import discord
import : The term 'import' is not recognized as the name of a cmdlet, function, script file, or operable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ import discord
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (import:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq> from discord.ext import commands
At line:1 char:1
+ from discord.ext import commands
+ ~~~~
The 'from' keyword is not supported in this version of the language.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : ReservedKeywordNotAllowed

PS C:\Users\shooq> import json
import : The term 'import' is not recognized as the name of a cmdlet, function, script file, or operable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ import json
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (import:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq> import os
import : The term 'import' is not recognized as the name of a cmdlet, function, script file, or operable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ import os
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (import:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq>
PS C:\Users\shooq> # إعدادات البوت والصلاحيات
PS C:\Users\shooq> intents = discord.Intents.default()
At line:1 char:35
+ intents = discord.Intents.default()
+                                   ~
An expression was expected after '('.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : ExpectedExpression

PS C:\Users\shooq> intents.guilds = True
intents.guilds : The term 'intents.guilds' is not recognized as the name of a cmdlet, function, script file, or
operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try
again.
At line:1 char:1
+ intents.guilds = True
+ ~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (intents.guilds:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq> intents.members = True  # مطلوب لتفعيل حدث دخول الأعضاء
intents.members : The term 'intents.members' is not recognized as the name of a cmdlet, function, script file, or
operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try
again.
At line:1 char:1
+ intents.members = True  # مطلوب لتفعيل حدث دخول الأعضاء
+ ~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (intents.members:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq>
PS C:\Users\shooq> bot = commands.Bot(command_prefix="!", intents=intents)
At line:1 char:38
+ bot = commands.Bot(command_prefix="!", intents=intents)
+                                      ~
Missing argument in parameter list.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingArgument

PS C:\Users\shooq>
PS C:\Users\shooq> # ملف حفظ الإعدادات
PS C:\Users\shooq> CONFIG_FILE = "config.json"
CONFIG_FILE : The term 'CONFIG_FILE' is not recognized as the name of a cmdlet, function, script file, or operable
program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ CONFIG_FILE = "config.json"
+ ~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (CONFIG_FILE:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq>
PS C:\Users\shooq> # تحميل الإعدادات أو إنشاء ملف افتراضي
PS C:\Users\shooq> def load_config():
At line:1 char:17
+ def load_config():
+                 ~
An expression was expected after '('.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : ExpectedExpression

PS C:\Users\shooq>     if not os.path.exists(CONFIG_FILE):
At line:1 char:7
+     if not os.path.exists(CONFIG_FILE):
+       ~
Missing '(' after 'if' in if statement.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingOpenParenthesisInIfStatement

PS C:\Users\shooq>         default_data = {"welcome_channel_id": None, "welcome_image": "https://i.imgur.com/A82X92g.png"}
At line:1 char:45
+         default_data = {"welcome_channel_id": None, "welcome_image":  ...
+                                             ~
Unexpected token ':' in expression or statement.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : UnexpectedToken

PS C:\Users\shooq>         with open(CONFIG_FILE, "w") as f:
At line:1 char:30
+         with open(CONFIG_FILE, "w") as f:
+                              ~
Missing argument in parameter list.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingArgument

PS C:\Users\shooq>             json.dump(default_data, f, indent=4)
At line:1 char:35
+             json.dump(default_data, f, indent=4)
+                                   ~
Missing argument in parameter list.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingArgument

PS C:\Users\shooq>     with open(CONFIG_FILE, "r") as f:
At line:1 char:26
+     with open(CONFIG_FILE, "r") as f:
+                          ~
Missing argument in parameter list.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingArgument

PS C:\Users\shooq>         return json.load(f)
f : The term 'f' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:26
+         return json.load(f)
+                          ~
    + CategoryInfo          : ObjectNotFound: (f:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq>
PS C:\Users\shooq> def save_config(data):
data : The term 'data' is not recognized as the name of a cmdlet, function, script file, or operable program. Check
the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:17
+ def save_config(data):
+                 ~~~~
    + CategoryInfo          : ObjectNotFound: (data:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq>     with open(CONFIG_FILE, "w") as f:
At line:1 char:26
+     with open(CONFIG_FILE, "w") as f:
+                          ~
Missing argument in parameter list.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingArgument

PS C:\Users\shooq>         json.dump(data, f, indent=4)
At line:1 char:23
+         json.dump(data, f, indent=4)
+                       ~
Missing argument in parameter list.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingArgument

PS C:\Users\shooq>
PS C:\Users\shooq> @bot.event
At line:1 char:1
+ @bot.event
+ ~~~~
The splatting operator '@' cannot be used to reference variables in an expression. '@bot' can be used only as an
argument to a command. To reference variables in an expression use '$bot'.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : SplattingNotPermitted

PS C:\Users\shooq> async def on_ready():
At line:1 char:20
+ async def on_ready():
+                    ~
An expression was expected after '('.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : ExpectedExpression

PS C:\Users\shooq>     print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
fLogged in as {bot.user.name} (ID: {bot.user.id}) : The term 'fLogged in as {bot.user.name} (ID: {bot.user.id})' is
not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or
if a path was included, verify that the path is correct and try again.
At line:1 char:11
+     print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
+           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (fLogged in as {... {bot.user.id}):String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq>     print("------")
Unable to initialize device PRN
PS C:\Users\shooq>
PS C:\Users\shooq> # كلاس القائمة المنسدلة لاختيار الروم
PS C:\Users\shooq> class ChannelSelectView(discord.ui.View):
At line:1 char:24
+ class ChannelSelectView(discord.ui.View):
+                        ~
Missing 'class' body in 'class' declaration.
At line:1 char:41
+ class ChannelSelectView(discord.ui.View):
+                                         ~
Unexpected token ':' in expression or statement.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingTypeBody

PS C:\Users\shooq>     def __init__(self):
self : The term 'self' is not recognized as the name of a cmdlet, function, script file, or operable program. Check
the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:18
+     def __init__(self):
+                  ~~~~
    + CategoryInfo          : ObjectNotFound: (self:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq>         super().__init__(timeout=180)
At line:1 char:15
+         super().__init__(timeout=180)
+               ~
An expression was expected after '('.
At line:1 char:26
+         super().__init__(timeout=180)
+                          ~
Missing ')' in method call.
At line:1 char:37
+         super().__init__(timeout=180)
+                                     ~
Unexpected token ')' in expression or statement.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : ExpectedExpression

PS C:\Users\shooq>
PS C:\Users\shooq>     @discord.ui.select(
>>         cls=discord.ui.ChannelSelect,
At line:1 char:24
+     @discord.ui.select(
+                        ~
Missing ')' in method call.
At line:2 char:9
+         cls=discord.ui.ChannelSelect,
+         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unexpected token 'cls=discord.ui.ChannelSelect' in expression or statement.
At line:2 char:37
+         cls=discord.ui.ChannelSelect,
+                                     ~
Missing argument in parameter list.
At line:1 char:5
+     @discord.ui.select(
+     ~~~~~~~~
The splatting operator '@' cannot be used to reference variables in an expression. '@discord' can be used only as an
argument to a command. To reference variables in an expression use '$discord'.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingEndParenthesisInMethodCall

PS C:\Users\shooq>         placeholder="اختر روم الترحيب من القائمة...",
At line:1 char:53
+         placeholder="اختر روم الترحيب من القائمة...",
+                                                     ~
Missing argument in parameter list.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingArgument

PS C:\Users\shooq>         channel_types=[discord.ChannelType.text],
At line:1 char:49
+         channel_types=[discord.ChannelType.text],
+                                                 ~
Missing argument in parameter list.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingArgument

PS C:\Users\shooq>         min_values=1,
At line:1 char:21
+         min_values=1,
+                     ~
Missing argument in parameter list.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingArgument

PS C:\Users\shooq>         max_values=1
max_values=1 : The term 'max_values=1' is not recognized as the name of a cmdlet, function, script file, or operable
program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:9
+         max_values=1
+         ~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (max_values=1:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq>     )
At line:1 char:5
+     )
+     ~
Unexpected token ')' in expression or statement.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : UnexpectedToken

PS C:\Users\shooq>     async def select_callback(self, interaction: discord.Interaction, select: discord.ui.ChannelSelect):
At line:1 char:35
+     async def select_callback(self, interaction: discord.Interaction, ...
+                                   ~
Missing argument in parameter list.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingArgument

PS C:\Users\shooq>         selected_channel = select.values[0]
selected_channel : The term 'selected_channel' is not recognized as the name of a cmdlet, function, script file, or
operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try
again.
At line:1 char:9
+         selected_channel = select.values[0]
+         ~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (selected_channel:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq>
PS C:\Users\shooq>         # حفظ الروم المختار في الملف
PS C:\Users\shooq>         config = load_config()
At line:1 char:30
+         config = load_config()
+                              ~
An expression was expected after '('.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : ExpectedExpression

PS C:\Users\shooq>         config["welcome_channel_id"] = selected_channel.id
config[welcome_channel_id] : The term 'config[welcome_channel_id]' is not recognized as the name of a cmdlet,
function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the
path is correct and try again.
At line:1 char:9
+         config["welcome_channel_id"] = selected_channel.id
+         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (config[welcome_channel_id]:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq>         save_config(config)
config : The term 'config' is not recognized as the name of a cmdlet, function, script file, or operable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:21
+         save_config(config)
+                     ~~~~~~
    + CategoryInfo          : ObjectNotFound: (config:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq>
PS C:\Users\shooq>         await interaction.response.send_message(
>>             f"✅ تم بنجاح تعيين روم الترحيب إلى: {selected_channel.mention}",
>>             ephemeral=True
>>         )
At line:2 char:76
+ ...      f"✅ تم بنجاح تعيين روم الترحيب إلى: {selected_channel.mention}",
+                                                                         ~
Missing argument in parameter list.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingArgument

PS C:\Users\shooq>
PS C:\Users\shooq> # أمر سلاش (Slash Command) لفتح القائمة المنسدلة
PS C:\Users\shooq> @bot.tree.command(name="setwelcome", description="اختر روم الترحيب عبر قائمة منسدلة")
At line:1 char:19
+ @bot.tree.command(name="setwelcome", description="اختر روم الترحيب عب ...
+                   ~
Missing ')' in method call.
At line:1 char:19
+ @bot.tree.command(name="setwelcome", description="اختر روم الترحيب عب ...
+                   ~~~~~~~~~~~~~~~~~
Unexpected token 'name="setwelcome"' in expression or statement.
At line:1 char:36
+ @bot.tree.command(name="setwelcome", description="اختر روم الترحيب عب ...
+                                    ~
Missing argument in parameter list.
At line:1 char:85
+ ... d(name="setwelcome", description="اختر روم الترحيب عبر قائمة منسدلة")
+                                                                         ~
Unexpected token ')' in expression or statement.
At line:1 char:1
+ @bot.tree.command(name="setwelcome", description="اختر روم الترحيب عب ...
+ ~~~~
The splatting operator '@' cannot be used to reference variables in an expression. '@bot' can be used only as an
argument to a command. To reference variables in an expression use '$bot'.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingEndParenthesisInMethodCall

PS C:\Users\shooq> @discord.app_commands.checks.has_permissions(administrator=True)
At line:1 char:46
+ @discord.app_commands.checks.has_permissions(administrator=True)
+                                              ~
Missing ')' in method call.
At line:1 char:46
+ @discord.app_commands.checks.has_permissions(administrator=True)
+                                              ~~~~~~~~~~~~~~~~~~
Unexpected token 'administrator=True' in expression or statement.
At line:1 char:64
+ @discord.app_commands.checks.has_permissions(administrator=True)
+                                                                ~
Unexpected token ')' in expression or statement.
At line:1 char:1
+ @discord.app_commands.checks.has_permissions(administrator=True)
+ ~~~~~~~~
The splatting operator '@' cannot be used to reference variables in an expression. '@discord' can be used only as an
argument to a command. To reference variables in an expression use '$discord'.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingEndParenthesisInMethodCall

PS C:\Users\shooq> async def setwelcome(interaction: discord.Interaction):
interaction: : The term 'interaction:' is not recognized as the name of a cmdlet, function, script file, or operable
program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:22
+ async def setwelcome(interaction: discord.Interaction):
+                      ~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (interaction::String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq>     view = ChannelSelectView()
At line:1 char:30
+     view = ChannelSelectView()
+                              ~
An expression was expected after '('.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : ExpectedExpression

PS C:\Users\shooq>     await interaction.response.send_message(
>>         "👇 يرجى اختيار روم الترحيب من القائمة أدناه:",
>>         view=view,
>>         ephemeral=True
At line:2 char:56
+         "👇 يرجى اختيار روم الترحيب من القائمة أدناه:",
+                                                        ~
Missing expression after ','.
At line:3 char:9
+         view=view,
+         ~~~~~~~~~
Unexpected token 'view=view' in expression or statement.
At line:2 char:56
+         "👇 يرجى اختيار روم الترحيب من القائمة أدناه:",
+                                                        ~
Missing closing ')' in expression.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingExpressionAfterToken

PS C:\Users\shooq>     )
At line:1 char:5
+     )
+     ~
Unexpected token ')' in expression or statement.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : UnexpectedToken

PS C:\Users\shooq>
PS C:\Users\shooq> # مزامنة أوامر السلاش عند التشغيل
PS C:\Users\shooq> @bot.event
At line:1 char:1
+ @bot.event
+ ~~~~
The splatting operator '@' cannot be used to reference variables in an expression. '@bot' can be used only as an
argument to a command. To reference variables in an expression use '$bot'.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : SplattingNotPermitted

PS C:\Users\shooq> async def setup_hook():
At line:1 char:22
+ async def setup_hook():
+                      ~
An expression was expected after '('.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : ExpectedExpression

PS C:\Users\shooq>     await bot.tree.sync()
At line:1 char:25
+     await bot.tree.sync()
+                         ~
An expression was expected after '('.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : ExpectedExpression

PS C:\Users\shooq>
PS C:\Users\shooq> # حدث دخول عضو جديد للسيرفر
PS C:\Users\shooq> @bot.event
At line:1 char:1
+ @bot.event
+ ~~~~
The splatting operator '@' cannot be used to reference variables in an expression. '@bot' can be used only as an
argument to a command. To reference variables in an expression use '$bot'.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : SplattingNotPermitted

PS C:\Users\shooq> async def on_member_join(member: discord.Member):
member: : The term 'member:' is not recognized as the name of a cmdlet, function, script file, or operable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:26
+ async def on_member_join(member: discord.Member):
+                          ~~~~~~~
    + CategoryInfo          : ObjectNotFound: (member::String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq>     config = load_config()
At line:1 char:26
+     config = load_config()
+                          ~
An expression was expected after '('.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : ExpectedExpression

PS C:\Users\shooq>     channel_id = config.get("welcome_channel_id")
channel_id : The term 'channel_id' is not recognized as the name of a cmdlet, function, script file, or operable
program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:5
+     channel_id = config.get("welcome_channel_id")
+     ~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (channel_id:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq>     image_url = config.get("welcome_image")
image_url : The term 'image_url' is not recognized as the name of a cmdlet, function, script file, or operable
program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:5
+     image_url = config.get("welcome_image")
+     ~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (image_url:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq>
PS C:\Users\shooq>     if not channel_id:
At line:1 char:7
+     if not channel_id:
+       ~
Missing '(' after 'if' in if statement.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingOpenParenthesisInIfStatement

PS C:\Users\shooq>         return
PS C:\Users\shooq>
PS C:\Users\shooq>     channel = member.guild.get_channel(channel_id)
channel_id : The term 'channel_id' is not recognized as the name of a cmdlet, function, script file, or operable
program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:40
+     channel = member.guild.get_channel(channel_id)
+                                        ~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (channel_id:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq>     if not channel:
At line:1 char:7
+     if not channel:
+       ~
Missing '(' after 'if' in if statement.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingOpenParenthesisInIfStatement

PS C:\Users\shooq>         return
PS C:\Users\shooq>
PS C:\Users\shooq>     # تصميم رسالة الترحيب (Embed)
PS C:\Users\shooq>     embed = discord.Embed(
>>         title="👋 أهلاً بك في السيرفر!",
>>         description=f"مرحباً بك {member.mention} في سيرفر **{member.guild.name}**!\nنحن سعداء جداً بانضمامك إلينا.",
>>         color=discord.Color.blurple()
>>     )
At line:2 char:40
+         title="👋 أهلاً بك في السيرفر!",
+                                        ~
Missing argument in parameter list.
At line:4 char:37
+         color=discord.Color.blurple()
+                                     ~
An expression was expected after '('.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingArgument

PS C:\Users\shooq>
PS C:\Users\shooq>     # صورة بروفايل العضو كصورة مصغرة
PS C:\Users\shooq>     if member.avatar:
At line:1 char:7
+     if member.avatar:
+       ~
Missing '(' after 'if' in if statement.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingOpenParenthesisInIfStatement

PS C:\Users\shooq>         embed.set_thumbnail(url=member.avatar.url)
url=member.avatar.url : The term 'url=member.avatar.url' is not recognized as the name of a cmdlet, function, script
file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct
and try again.
At line:1 char:29
+         embed.set_thumbnail(url=member.avatar.url)
+                             ~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (url=member.avatar.url:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq>
PS C:\Users\shooq>     # صورة الترحيب المخصصة الكبيرة
PS C:\Users\shooq>     if image_url:
At line:1 char:7
+     if image_url:
+       ~
Missing '(' after 'if' in if statement.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingOpenParenthesisInIfStatement

PS C:\Users\shooq>         embed.set_image(url=image_url)
url=image_url : The term 'url=image_url' is not recognized as the name of a cmdlet, function, script file, or operable
program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:25
+         embed.set_image(url=image_url)
+                         ~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (url=image_url:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq>
PS C:\Users\shooq>     embed.set_footer(text=f"رقم العضو: {member.guild.member_count}")
text=fرقم العضو: {member.guild.member_count} : The term 'text=fرقم العضو: {member.guild.member_count}' is not
recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if
a path was included, verify that the path is correct and try again.
At line:1 char:22
+     embed.set_footer(text=f"رقم العضو: {member.guild.member_count}")
+                      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (text=fرقم العضو...d.member_count}:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\shooq>
PS C:\Users\shooq>     # إرسال الرسالة
PS C:\Users\shooq>     await channel.send(content=f"{member.mention}", embed=embed)
At line:1 char:51
+     await channel.send(content=f"{member.mention}", embed=embed)
+                                                   ~
Missing argument in parameter list.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingArgument

import os
client.run(os.getenv("TOKEN"))
