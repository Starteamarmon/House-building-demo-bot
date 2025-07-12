from bojango.core.routing import callback
from bojango.action.screen import ActionScreen, ScreenType, ActionButton
from bojango.action.dispatcher import ActionManager
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext


@callback('s_start')
async def s_start(update, context):
    yield ActionScreen(text='''**Приветствуем!** Мы строим дома **под ключ**:

🧱 **Кирпичные** | 🪵 **Каркасные** | 🏠 **Модульные**

Давайте подберём идеальный вариант для вас.  
Ответьте на несколько коротких вопросов — это займёт *1–2 минуты* 🙌
''', buttons=[
    [ ActionButton(text='🔘 Кирпичный', action_name='s_brick')],
    [ ActionButton(text='🔘 Каркасный', action_name='s_frame')],
    [ActionButton(text='🔘 Модульный', action_name='s_modular')],
    [ActionButton(text='🔘 Ещё не определился', action_name='s_undecided')],[ActionButton(text='📸 Примеры работ', action_name='s_examples')]
])


@callback('s_undecided')
async def s_examples(update, context):
    yield ActionScreen(
        text=(
            '''Ничего страшного! Мы поможем подобрать оптимальный тип по 
бюджету и задачам. 
Перейдём к следующему вопросу? '''
        ),
        buttons=[
            [ActionButton(text='🔘 Да', action_name='s_square')],
            [ActionButton(text='🔘 Выйти', action_name='s_start')]
        ]
    )


@callback('s_examples')
async def s_examples(update, context):
    yield ActionScreen(
        text=(
            '📸 Вот примеры наших реализованных проектов:\n'
            '👉 [Посмотреть](https://github.com/Starteamarmon)\n\n'
            'Продолжим подбор?'
        ),
        buttons=[
            [ActionButton(text='🔘 Да', action_name='s_start')],
            [ActionButton(text='🔘 Выйти', action_name='s_start')]
        ]
    )


@callback('s_brick')
async def s_brick(update, context):
    yield ActionScreen(text='''🧱 Кирпичные дома — это долговечность, прочность и 
классический внешний вид. 
Отлично подходят для постоянного проживания. 
                       
✅ Срок службы: 50+ лет 
✅ Тепло- и шумоизоляция 
✅ Возможность нестандартной архитектуры
                       
Продолжим?''',buttons=[[ActionButton(text='🔘 Да, подходит', action_name='s_square')], [ActionButton(text='🔘 Назад', action_name='s_start')]])
    

@callback('s_frame')
async def s_brick(update, context):
    yield ActionScreen(text='''Каркасные дома — тёплые, энергоэффективные, быстро 
строятся. 
                       
✅ Строим от 3 месяцев 
✅ Экономия на отоплении 
✅ Гарантия 10 лет 
                       
Продолжим?''',buttons=[[ActionButton(text='🔘 Да, подходит', action_name='s_square')], [ActionButton(text='🔘 Назад', action_name='s_start')]])
    

@callback('s_modular')
async def s_brick(update, context):
    yield ActionScreen(text='''Модульные дома — современное решение для дачи или 
постоянного проживания. 
Собираются на участке за считанные дни.  
                       
✅ Минимум подготовки  
✅ Быстрый монтаж 
✅ Можно перевезти
                       
Продолжим?''',buttons=[[ActionButton(text='🔘 Да, подходит', action_name='s_square')], [ActionButton(text='🔘 Назад', action_name='s_start')]])
    

@callback('s_square')
async def s_square(update, context):
    yield ActionScreen(text='Примерная площадь дома?', buttons=[
        [ActionButton(text='🔘  до 100 м²',action_name='s_plot')],
        [ActionButton(text='🔘 100–150 м²',action_name='s_plot')],
        [ActionButton(text='🔘 150–200 м²',action_name='s_plot')],
        [ActionButton(text='🔘 более 200 м²',action_name='s_plot')],
        [ActionButton(text='🔘 Пока не знаю',action_name='s_plot')],
    ])


@callback('s_plot')
async def s_plot(update, context):
    yield ActionScreen(text='У вас уже есть участок под строительство?', buttons=[
        [ActionButton(text='🔘 Да',action_name='s_budget')],
        [ActionButton(text='🔘 В процессу покупки',action_name='s_budget')],
        [ActionButton(text='🔘 Пока нет',action_name='s_budget')],
        [ActionButton(text='🔘 Нужна помощь с подбором',action_name='s_budget')]
    ])


@callback('s_budget')
async def s_budget(update, context):
    yield ActionScreen(text='Какой ориентировочный бюджет?', buttons=[
        [ActionButton(text='🔘 до 3 млн ₽',action_name='s_deadlines')],
        [ActionButton(text='🔘 3–5 млн ₽',action_name='s_deadlines')],
        [ActionButton(text='🔘 5–8 млн ₽ ',action_name='s_deadlines')],
        [ActionButton(text='🔘 более 8 млн ₽',action_name='s_deadlines')],
        [ActionButton(text='🔘 Пока не решил(а)',action_name='s_deadlines')],
    ])


@callback('s_deadlines')
async def s_deadlines(update, context):
    yield ActionScreen(text='Когда планируете начать строительство?', buttons=[
        [ActionButton(text='🔘 В ближайшие 1–2 месяца ',action_name='s_comment_optional')],
        [ActionButton(text='🔘 Через 3–6 месяцев',action_name='s_comment_optional')],
        [ActionButton(text='🔘 Через год',action_name='s_comment_optional')],
        [ActionButton(text='🔘 Просто интересуюсь',action_name='s_comment_optional')]
    ])



###
@callback('s_comment_optional')
async def s_comment_optional(update, context):
    # Сохраняем состояние ожидания ввода комментария
    context.user_data['awaiting'] = 'comment'

    yield ActionScreen(
        text="✍️ Хотите оставить комментарий, пожелания или задать вопрос?\n\n(Можно пропустить)",
        buttons=[
            [ActionButton(text="Пропустить", action_name="s_contacts")],
        ]
    )


###
@callback('s_comment_save')
async def s_comment_save(update, context):
    print('Дошло')
    yield ActionScreen(
            text="✅ Комментарий сохранён.",
            buttons=[[ActionButton(text="Далее", action_name="s_contacts")]]
        )
    

@callback('s_contacts')
async def s_phone(update, context):
    context.user_data['awaiting'] = 'phone'
    yield ActionScreen(
        text='''Почти готово! Оставьеу, пожалуйста, ваши контактные данные
— мы свяжемся и проконсультируем вас:
📱 Введите номер телефона: +7XXXXXXXXXX'''
)


@callback('s_name')
async def s_name(update, context):
    context.user_data['awaiting'] = 'name'
    yield ActionScreen(text='🧒🏻 Как вас зовут?')


@callback('s_finale')
async def s_finale(update, context):
    name = context.user_data.get('u_name')
    yield ActionScreen(text=f'''Спасибо, {name}! Мы получили вашу заявку.
Наш специалист свяжется с вами в ближайшее время 📞
📸 Пока можно посмотреть ещё примеры работ:
👉 [Перейти на сайт](https://github.com/Starteamarmon)''')