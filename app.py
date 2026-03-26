import streamlit as st

st.set_page_config(page_title="ウェクスラー風・知能測定", layout="centered")

st.title("🧠 知能測定ミニテスト (WAIS要素準拠)")
st.write("論理、計算、言語、ワーキングメモリを測定します。全10問です。")

# 問題データ
questions = [
    {
        "type": "類似",
        "q": "「自由」と「規律」の共通点は何ですか？",
        "options": ["どちらも社会のルール", "どちらも概念である", "どちらも反対の意味", "どちらも大切なもの"],
        "answer": "どちらも概念である",
        "expl": "より高い抽象度で共通点を見つける能力を測ります。"
    },
    {
        "type": "算数",
        "q": "時速60kmの車が、15分間で進む距離は何kmですか？",
        "options": ["10km", "15km", "20km", "4km"],
        "answer": "15km",
        "expl": "暗算能力と論理的な処理速度を測ります。"
    },
    {
        "type": "行列推理",
        "q": "次の数列の法則を見つけてください： 1, 3, 7, 15, 31, (?)",
        "options": ["62", "63", "46", "55"],
        "answer": "63",
        "expl": "前の数を2倍して1を足す（n*2+1）というパターン推論です。"
    },
    {
        "type": "ワーキングメモリ",
        "q": "バラバラの文字「り」「し」「と」「り」「き」を並べ替えてできる『機械』は何？",
        "options": ["しりとりき", "とりしりき", "ちりとりき", "きりとりき"],
        "answer": "きりとりき"
    },
    {
        "type": "知識",
        "q": "「一石二鳥」と同じ意味の四字熟語はどれですか？",
        "options": ["一挙両得", "因果応報", "千載一遇", "五里霧中"],
        "answer": "一挙両得",
        "expl": "習得した知識と言語の理解力を測ります。"
    },
    {
        "type": "論理",
        "q": "「AはBより大きく、BはCより小さい。AがCより大きい」という結論は？",
        "options": ["必ず正しい", "必ず間違い", "正しいとは限らない", "Bが一番大きい"],
        "answer": "正しいとは限らない",
        "expl": "A>B, C>B という情報だけでは、AとCの比較は確定できません。"
    },
    {
        "type": "行列推理",
        "q": "「日：月 ＝ 1：31」であるとき、「月：年」は？",
        "options": ["1：12", "1：365", "1：7", "1：24"],
        "answer": "1：12",
        "expl": "時間概念の包含関係を正しく類論する力を測ります。"
    },
    {
        "type": "単語",
        "q": "「杞憂（きゆう）」の正しい意味は？",
        "options": ["無意味な心配", "深い悲しみ", "突然の災難", "計画的な行動"],
        "answer": "無意味な心配",
        "expl": "語彙の豊かさを測ります。"
    },
    {
        "type": "算数",
        "q": "ある商品の価格を20%引きし、その後10%値上げしました。元の価格と比較すると？",
        "options": ["10%引きと同じ", "12%引きと同じ", "8%引きと同じ", "変わらない"],
        "answer": "12%引きと同じ",
        "expl": "100 * 0.8 * 1.1 = 88。12%引きの状態です。"
    },
    {
        "type": "ワーキングメモリ",
        "q": "「3-8-2-5」という数字を、逆から（後ろから）順番に言うと？",
        "options": ["5-2-8-3", "5-8-2-3", "3-2-8-5", "2-5-8-3"],
        "answer": "5-2-8-3",
        "expl": "逆唱能力はワーキングメモリの代表的な指標です。"
    }
]

# セッション状態の初期化
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.score = 0
    st.session_state.finished = False

# テスト画面
if not st.session_state.finished:
    q_idx = st.session_state.step
    q_data = questions[q_idx]
    
    st.progress((q_idx) / len(questions))
    st.subheader(f"問 {q_idx + 1} [{q_data['type']}]")
    st.write(q_data['q'])
    
    # 回答選択肢
    choice = st.radio("答えを選択してください：", q_data['options'], index=None, key=f"q_{q_idx}")
    
    if st.button("次へ"):
        if choice == q_data['answer']:
            st.session_state.score += 1
        
        if q_idx + 1 < len(questions):
            st.session_state.step += 1
            st.rerun()
        else:
            st.session_state.finished = True
            st.rerun()

# 結果表示
else:
    st.balloons()
    st.header("測定完了！")
    score = st.session_state.score
    total = len(questions)
    
    st.metric(label="正解数", value=f"{score} / {total}")
    
    if score == 10:
        st.success("完璧です！非常に高い知的能力（WAIS換算 130相当）の可能性があります。")
    elif score >= 7:
        st.info("平均より高いスコアです。論理的思考に優れています。")
    else:
        st.warning("平均的なスコアです。落ち着いて考えればもっと伸びるはずです。")

    if st.button("もう一度受ける"):
        st.session_state.step = 0
        st.session_state.score = 0
        st.session_state.finished = False
        st.rerun()
