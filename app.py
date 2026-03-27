import streamlit as st

st.set_page_config(page_title="知能測定プロ 15", layout="centered")

# --- 問題データ定義（全15問） ---
if 'questions' not in st.session_state:
    st.session_state.questions = [
        {"type": "類似", "q": "「自由」と「規律」の共通点は？", "options": ["反対の意味", "社会生活における個人のあり方", "法律の別名", "感情の種類"], "answer": "社会生活における個人のあり方", "expl": "どちらも集団の中で個人がどう振る舞うかを示す概念です。"},
        {"type": "算数", "q": "時速60kmの車が15分で進む距離は？", "options": ["10km", "15km", "20km", "4km"], "answer": "15km", "expl": "60km/h = 1km/分。15分なら15kmです。"},
        {"type": "行列", "q": "1, 3, 7, 15, 31, (?) 次の数字は？", "options": ["62", "63", "46", "55"], "answer": "63", "expl": "前の数を2倍して1を足す（n*2+1）法則です。"},
        {"type": "WM", "q": "「ち」「り」「り」「と」「き」を並べ替えてできる道具は？", "options": ["ちりとりき", "きりとりち", "とりちりき", "りきりとう"], "answer": "ちりとりき", "expl": "正解は「ちりとり（機）」です。"},
        {"type": "知識", "q": "「一石二鳥」と最も近い意味は？", "options": ["一挙両得", "因果応報", "千載一遇", "五里霧中"], "answer": "一挙両得", "expl": "一つの行為で二つの利益を得るという意味です。"},
        {"type": "論理", "q": "A>B, B>C のとき、必ず言えることは？", "options": ["A>C", "A<C", "A=C", "判断不可"], "answer": "A>C", "expl": "三段論法により、AはCより必ず大きくなります。"},
        {"type": "概念", "q": "「1ヶ月：1年 ＝ 1：12」が表す関係は？", "options": ["構成要素と全体", "時間の速さ", "日付の合計", "偶然"], "answer": "構成要素と全体", "expl": "12個の月が集まって1個の年を作る「内訳」の関係です。"},
        {"type": "単語", "q": "「杞憂」の正しい意味は？", "options": ["無意味な心配", "深い悲しみ", "災難", "計画的行動"], "answer": "無意味な心配", "expl": "起こりもしないことを心配することです。"},
        {"type": "論理", "q": "「昨日が明日なら今日は金曜日」のとき、現実は何曜日？", "options": ["水曜日", "金曜日", "日曜日", "土曜日"], "answer": "日曜日", "expl": "仮定の明日＝金曜（仮定の今日＝木曜）。現実の昨日＝木曜なので現実は日曜。"},
        {"type": "算数", "q": "100円を20%引きし、その後10%値上げすると？", "options": ["90円", "88円", "92円", "100円"], "answer": "88円", "expl": "100 * 0.8 = 80。 80 * 1.1 = 88 です。"},
        {"type": "類似", "q": "「山」と「川」の共通点は？", "options": ["動かないもの", "自然の地形", "飲み水", "観光地"], "answer": "自然の地形", "expl": "どちらも地球の表面を構成する自然の造形物です。"},
        {"type": "行列", "q": "1, 1, 2, 3, 5, 8, (?) 次の数字は？", "options": ["11", "13", "15", "10"], "answer": "13", "expl": "フィボナッチ数列（前の2つを足す）です。"},
        {"type": "WM", "q": "「8-2-5-9」を後ろから言うと？", "options": ["9-5-2-8", "9-2-5-8", "8-5-2-9", "2-5-8-9"], "answer": "9-5-2-8", "expl": "逆唱はワーキングメモリの基本課題です。"},
        {"type": "知識", "q": "「情けは人のためならず」の正しい意味は？", "options": ["人のためにならない", "巡り巡って自分に返る", "情けは無用", "甘やかすな"], "answer": "巡り巡って自分に返る", "expl": "良い行いは自分に返ってくるという意味です。"},
        {"type": "論理", "q": "すべての人間は死ぬ。ソクラテスは人間だ。ならば？", "options": ["ソクラテスは死ぬ", "人間はソクラテスだ", "死ぬのは人間だけ", "判断不可"], "answer": "ソクラテスは死ぬ", "expl": "アリストテレスの三段論法の典型例です。"}
    ]

# --- セッション状態管理 ---
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.score = 0
    st.session_state.user_answers = []
    st.session_state.finished = False

# --- メイン画面 ---
if not st.session_state.finished:
    st.title("🧠 知能測定ミニテスト 15")
    q_idx = st.session_state.step
    q_data = st.session_state.questions[q_idx]
    
    st.progress(q_idx / 15)
    st.subheader(f"問 {q_idx + 1} / 15 [{q_data['type']}]")
    st.write(q_data['q'])
    
    choice = st.radio("答えを選択：", q_data['options'], index=None, key=f"q_{q_idx}")
    
    if st.button("次へ進む"):
        if choice is None:
            st.warning("回答を選んでください。")
        else:
            st.session_state.user_answers.append(choice)
            if choice == q_data['answer']:
                st.session_state.score += 1
            
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
    st.metric(label="正解数", value=f"{st.session_state.score} / 15")
    
    st.divider()
    st.subheader("📝 答え合わせと解説")
    
    for i, q in enumerate(st.session_state.questions):
        user_ans = st.session_state.user_answers[i]
        is_correct = (user_ans == q['answer'])
        
        color = "green" if is_correct else "red"
        mark = "✅" if is_correct else "❌"
        
        with st.expander(f"問 {i+1}: {mark} {q['q'][:20]}..."):
            st.write(f"**あなたの回答:** {user_ans}")
            st.write(f"**正解:** {q['answer']}")
            st.info(f"**解説:** {q['expl']}")

    if st.button("トップへ戻る"):
        st.session_state.step = 0
        st.session_state.score = 0
        st.session_state.user_answers = []
        st.session_state.finished = False
        st.rerun()
