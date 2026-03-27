import streamlit as st

st.set_page_config(page_title="精密・知能測定プロ", layout="centered")

# --- 問題データ定義（重み付け：weightを追加） ---
if 'questions' not in st.session_state:
    st.session_state.questions = [
        {"type": "類似", "weight": 1, "q": "「自由」と「規律」の共通点は？", "options": ["反対の意味", "社会生活における個人のあり方", "法律の別名", "感情の種類"], "answer": "社会生活における個人のあり方", "expl": "抽象的な概念の共通点を見抜く力を測ります。"},
        {"type": "算数", "weight": 2, "q": "時速60kmの車が15分で進む距離は？", "options": ["10km", "15km", "20km", "4km"], "answer": "15km", "expl": "単位換算と数値処理の速度を測ります。"},
        {"type": "行列", "weight": 2, "q": "1, 3, 7, 15, 31, (?) 次の数字は？", "options": ["62", "63", "46", "55"], "answer": "63", "expl": "非言語的な法則推論能力を測ります。"},
        {"type": "WM", "weight": 2, "q": "「ち」「り」「り」「と」「き」を並べ替えてできる道具は？", "options": ["ちりとりき", "きりとりち", "とりちりき", "りきりとう"], "answer": "ちりとりき", "expl": "脳内での情報操作能力を測ります。"},
        {"type": "知識", "weight": 1, "q": "「一石二鳥」と最も近い意味は？", "options": ["一挙両得", "因果応報", "千載一遇", "五里霧中"], "answer": "一挙両得", "expl": "言語的な知識の蓄積を測ります。"},
        {"type": "論理", "weight": 2, "q": "A>B, B>C のとき、必ず言えることは？", "options": ["A>C", "A<C", "A=C", "判断不可"], "answer": "A>C", "expl": "基本的な三段論法の理解を測ります。"},
        {"type": "概念", "weight": 1, "q": "「1ヶ月：1年 ＝ 1：12」が表す関係は？", "options": ["構成要素と全体", "時間の速さ", "日付の合計", "偶然"], "answer": "構成要素と全体", "expl": "事象の包含関係を正しく認識する力を測ります。"},
        {"type": "単語", "weight": 1, "q": "「杞憂」の正しい意味は？", "options": ["無意味な心配", "深い悲しみ", "災難", "計画的行動"], "answer": "無意味な心配", "expl": "語彙力の豊かさを測ります。"},
        {"type": "論理", "weight": 3, "q": "「昨日が明日なら今日は金曜日」のとき、現実は何曜日？", "options": ["水曜日", "金曜日", "日曜日", "土曜日"], "answer": "日曜日", "expl": "高度な時間的・論理的推論力を測る難問です。"},
        {"type": "算数", "weight": 3, "q": "100円を20%引きし、その後10%値上げすると？", "options": ["90円", "88円", "92円", "100円"], "answer": "88円", "expl": "割合の連続変化を正確に処理する能力を測ります。"},
        {"type": "類似", "weight": 1, "q": "「山」と「川」の共通点は？", "options": ["動かないもの", "自然の地形", "飲み水", "観光地"], "answer": "自然の地形", "expl": "具体的な物体の共通カテゴリーを抽出する力を測ります。"},
        {"type": "行列", "weight": 2, "q": "1, 1, 2, 3, 5, 8, (?) 次の数字は？", "options": ["11", "13", "15", "10"], "answer": "13", "expl": "変則的な数列の法則性を発見する力を測ります。"},
        {"type": "WM", "weight": 3, "q": "「8-2-5-9」を後ろから言うと？", "options": ["9-5-2-8", "9-2-5-8", "8-5-2-9", "2-5-8-9"], "answer": "9-5-2-8", "expl": "情報の逆転操作を行うワーキングメモリの難問です。"},
        {"type": "知識", "weight": 1, "q": "「情けは人のためならず」の正しい意味は？", "options": ["人のためにならない", "巡り巡って自分に返る", "情けは無用", "甘やかすな"], "answer": "巡り巡って自分に返る", "expl": "慣用句の正確な知識を測ります。"},
        {"type": "論理", "weight": 2, "q": "すべての人間は死ぬ。ソクラテスは人間だ。ならば？", "options": ["ソクラテスは死ぬ", "人間はソクラテスだ", "死ぬのは人間だけ", "判断不可"], "answer": "ソクラテスは死ぬ", "expl": "演繹的な論理展開能力を測ります。"}
    ]

# --- セッション状態管理 ---
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.weighted_score = 0
    st.session_state.user_answers = []
    st.session_state.finished = False

# 総ポイント数の計算（最大ポイント）
max_points = sum(q['weight'] for q in st.session_state.questions)

# --- メイン画面 ---
if not st.session_state.finished:
    st.title("🧠 精密・知能測定プロ 15")
    q_idx = st.session_state.step
    q_data = st.session_state.questions[q_idx]
    
    st.progress(q_idx / 15)
    st.subheader(f"問 {q_idx + 1} / 15 [{q_data['type']}]")
    st.write(q_data['q'])
    st.caption(f"配点: {q_data['weight']}pt")
    
    choice = st.radio("答えを選択：", q_data['options'], index=None, key=f"q_{q_idx}")
    
    if st.button("次へ進む"):
        if choice is None:
            st.warning("回答を選んでください。")
        else:
            st.session_state.user_answers.append(choice)
            if choice == q_data['answer']:
                st.session_state.weighted_score += q_data['weight']
            
            if q_idx + 1 < 15:
                st.session_state.step += 1
                st.rerun()
            else:
                st.session_state.finished = True
                st.rerun()

# --- 結果・答え合わせ画面 ---
else:
    st.balloons()
    st.header("🏁 測定完了！")
    
    actual_score = st.session_state.weighted_score
    # スコアの達成率に基づいた推定IQ（簡易計算式）
    # 達成率100%でIQ140、50%でIQ100程度にマッピング
    iq_est = 70 + (actual_score / max_points) * 70
    
    st.metric(label="獲得ポイント / 総ポイント", value=f"{actual_score} / {max_points}")
    st.metric(label="推定IQ(精密)", value=f"{int(iq_est)} 前後")
    
    if iq_est >= 130:
        st.success("【天才級】全領域において極めて高い知能を持っています。")
    elif iq_est >= 115:
        st.info("【優秀】非常に高い論理的思考力とWMを持っています。")
    elif iq_est >= 90:
        st.warning("【平均】標準的な知的能力です。")
    else:
        st.error("【平均以下】落ち着いて再挑戦してみましょう。")

    st.divider()
    st.subheader("📝 答え合わせと解説")
    
    for i, q in enumerate(st.session_state.questions):
        user_ans = st.session_state.user_answers[i]
        is_correct = (user_ans == q['answer'])
        mark = "✅" if is_correct else "❌"
        with st.expander(f"問 {i+1} ({q['weight']}pt): {mark} {q['q'][:20]}..."):
            st.write(f"**正解:** {q['answer']}")
            st.info(f"**解説:** {q['expl']}")

    if st.button("トップへ戻る"):
        st.session_state.step = 0
        st.session_state.weighted_score = 0
        st.session_state.user_answers = []
        st.session_state.finished = False
        st.rerun()
