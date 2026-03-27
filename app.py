import streamlit as st

st.set_page_config(page_title="WAIS風知能測定アプリ", layout="centered")

# =========================
# 問題データ
# =========================
QUESTIONS = [
    # ================= VCI =================
    {
        "id": 1,
        "domain": "VCI",
        "domain_label": "言語理解",
        "subtype": "類似",
        "difficulty": 1,
        "weight": 1,
        "q": "「自由」と「規律」の共通点は？",
        "options": [
            "反対の意味",
            "社会生活における個人のあり方",
            "法律の別名",
            "感情の種類"
        ],
        "answer": "社会生活における個人のあり方",
        "expl": "抽象概念の共通点を見抜く問題です。"
    },
    {
        "id": 2,
        "domain": "VCI",
        "domain_label": "言語理解",
        "subtype": "語彙",
        "difficulty": 1,
        "weight": 1,
        "q": "「杞憂」の正しい意味は？",
        "options": [
            "無意味な心配",
            "深い悲しみ",
            "災難",
            "計画的な行動"
        ],
        "answer": "無意味な心配",
        "expl": "語彙の意味を正確に把握できているかを見ます。"
    },
    {
        "id": 3,
        "domain": "VCI",
        "domain_label": "言語理解",
        "subtype": "ことわざ",
        "difficulty": 2,
        "weight": 2,
        "q": "「情けは人のためならず」の正しい意味は？",
        "options": [
            "人に親切にしても無駄",
            "甘やかすのはよくない",
            "人への親切は巡って自分に返る",
            "情けをかけてはいけない"
        ],
        "answer": "人への親切は巡って自分に返る",
        "expl": "ことわざ・慣用句の正確な理解を測ります。"
    },

    # ================= PRI =================
    {
        "id": 4,
        "domain": "PRI",
        "domain_label": "知覚推理",
        "subtype": "数列",
        "difficulty": 1,
        "weight": 1,
        "q": "1, 3, 7, 15, 31, (?) 次の数字は？",
        "options": ["62", "63", "46", "55"],
        "answer": "63",
        "expl": "前の数を2倍して1を足す規則です。"
    },
    {
        "id": 5,
        "domain": "PRI",
        "domain_label": "知覚推理",
        "subtype": "数列",
        "difficulty": 1,
        "weight": 1,
        "q": "1, 1, 2, 3, 5, 8, (?) 次の数字は？",
        "options": ["11", "13", "15", "10"],
        "answer": "13",
        "expl": "前2つの数を足すフィボナッチ型の数列です。"
    },
    {
        "id": 6,
        "domain": "PRI",
        "domain_label": "知覚推理",
        "subtype": "論理",
        "difficulty": 2,
        "weight": 2,
        "q": "A > B、B > C のとき、必ず言えることは？",
        "options": ["A > C", "A < C", "A = C", "判断できない"],
        "answer": "A > C",
        "expl": "大小関係の推移性を使う問題です。"
    },

    # ================= WMI =================
    {
        "id": 7,
        "domain": "WMI",
        "domain_label": "ワーキングメモリ",
        "subtype": "逆唱",
        "difficulty": 1,
        "weight": 1,
        "q": "「8-2-5-9」を後ろから言うと？",
        "options": ["9-5-2-8", "9-2-5-8", "8-5-2-9", "2-5-8-9"],
        "answer": "9-5-2-8",
        "expl": "保持した情報を逆順に操作する問題です。"
    },
    {
        "id": 8,
        "domain": "WMI",
        "domain_label": "ワーキングメモリ",
        "subtype": "並べ替え",
        "difficulty": 2,
        "weight": 2,
        "q": "「き」「ん」「え」「ぴ」「つ」を並べ替えてできる言葉は？",
        "options": ["えんぴつ", "きんぴつ", "つんえぴ", "ぴつえん"],
        "answer": "えんぴつ",
        "expl": "短期保持しながら正しい語に組み替える問題です。"
    },
    {
        "id": 9,
        "domain": "WMI",
        "domain_label": "ワーキングメモリ",
        "subtype": "暗算",
        "difficulty": 2,
        "weight": 2,
        "q": "7に5を足して、その結果から3を引くと？",
        "options": ["7", "8", "9", "10"],
        "answer": "9",
        "expl": "頭の中で順番に処理できるかを測ります。"
    },

    # ================= PSI =================
    {
        "id": 10,
        "domain": "PSI",
        "domain_label": "処理速度",
        "subtype": "照合",
        "difficulty": 1,
        "weight": 1,
        "q": "次のうち、他と異なるものはどれ？",
        "options": ["AB12", "AB12", "AB21", "AB12"],
        "answer": "AB21",
        "expl": "素早く違いを見つける力を測る問題です。"
    },
    {
        "id": 11,
        "domain": "PSI",
        "domain_label": "処理速度",
        "subtype": "比較",
        "difficulty": 1,
        "weight": 1,
        "q": "次のうち、最も大きい数は？",
        "options": ["98", "89", "108", "99"],
        "answer": "108",
        "expl": "単純な比較を素早く正確に行う問題です。"
    },
    {
        "id": 12,
        "domain": "PSI",
        "domain_label": "処理速度",
        "subtype": "照合",
        "difficulty": 2,
        "weight": 2,
        "q": "次のうち、完全に同じ並びはどれ？  『K7M2』",
        "options": ["K7N2", "K7M2", "KM72", "K2M7"],
        "answer": "K7M2",
        "expl": "視覚的な照合の正確さを測る問題です。"
    },
]

DOMAINS = ["VCI", "PRI", "WMI", "PSI"]
DOMAIN_LABELS = {
    "VCI": "言語理解",
    "PRI": "知覚推理",
    "WMI": "ワーキングメモリ",
    "PSI": "処理速度",
}


# =========================
# ユーティリティ
# =========================
def get_domain_max_scores(questions):
    max_scores = {domain: 0 for domain in DOMAINS}
    for q in questions:
        max_scores[q["domain"]] += q["weight"]
    return max_scores


def convert_domain_score(raw_score, max_score):
    """素点を指数(70〜130)に簡易変換"""
    if max_score == 0:
        return 70
    ratio = raw_score / max_score
    return round(70 + ratio * 60)


def calc_fsiq(domain_indices):
    """4領域指数から総合IQを算出"""
    return round(
        domain_indices["VCI"] * 0.30 +
        domain_indices["PRI"] * 0.30 +
        domain_indices["WMI"] * 0.20 +
        domain_indices["PSI"] * 0.20
    )


def get_iq_band_comment(iq):
    if iq >= 130:
        return "非常に高い"
    if iq >= 120:
        return "高い"
    if iq >= 110:
        return "やや高い"
    if iq >= 90:
        return "平均域"
    if iq >= 80:
        return "やや低い"
    return "低い"


def get_domain_comment(domain, score):
    if domain == "VCI":
        if score >= 120:
            return "言語理解・語彙・抽象化が強い傾向があります。"
        elif score >= 100:
            return "言語理解はおおむね安定しています。"
        else:
            return "語彙や概念理解の問題で伸びしろがあります。"

    if domain == "PRI":
        if score >= 120:
            return "法則発見や非言語推理が強い傾向があります。"
        elif score >= 100:
            return "パターン認識は標準的です。"
        else:
            return "数列や規則発見を鍛える余地があります。"

    if domain == "WMI":
        if score >= 120:
            return "情報保持と脳内操作が得意です。"
        elif score >= 100:
            return "ワーキングメモリは標準的です。"
        else:
            return "頭の中での保持や並べ替え課題で伸びしろがあります。"

    if domain == "PSI":
        if score >= 120:
            return "視覚探索や単純処理の速さ・正確さが高いです。"
        elif score >= 100:
            return "処理速度は標準的です。"
        else:
            return "素早い比較や照合課題で伸びしろがあります。"

    return ""


# =========================
# セッション初期化
# =========================
if "started" not in st.session_state:
    st.session_state.started = False

if "current_index" not in st.session_state:
    st.session_state.current_index = 0

if "answers" not in st.session_state:
    st.session_state.answers = []

if "raw_scores" not in st.session_state:
    st.session_state.raw_scores = {domain: 0 for domain in DOMAINS}

if "finished" not in st.session_state:
    st.session_state.finished = False


# =========================
# 開始画面
# =========================
if not st.session_state.started:
    st.title("🧠 WAIS風知能測定アプリ")
    st.subheader("4領域プロフィール版（簡易MVP）")

    st.write("""
このアプリでは、以下の4領域を簡易的に測定します。

- **VCI**：言語理解
- **PRI**：知覚推理
- **WMI**：ワーキングメモリ
- **PSI**：処理速度
""")

    st.warning("※ 本アプリは正式な臨床用知能検査ではありません。WAISを参考にした独自の簡易推定モデルです。")
    st.info("まずはタイマーなし・固定問題版の最小構成です。")

    if st.button("開始する"):
        st.session_state.started = True
        st.rerun()


# =========================
# 問題画面
# =========================
elif not st.session_state.finished:
    q_idx = st.session_state.current_index
    q = QUESTIONS[q_idx]

    total_questions = len(QUESTIONS)
    current_domain = q["domain"]
    current_domain_label = q["domain_label"]

    st.title("📝 問題に回答してください")
    st.progress(q_idx / total_questions)

    st.caption(f"領域: {current_domain} / {current_domain_label}")
    st.subheader(f"問 {q_idx + 1} / {total_questions}")
    st.write(f"**問題タイプ:** {q['subtype']}")
    st.write(f"**配点:** {q['weight']}点")
    st.write("---")
    st.write(q["q"])

    choice = st.radio(
        "答えを選んでください",
        q["options"],
        index=None,
        key=f"question_{q_idx}"
    )

    if st.button("次へ"):
        if choice is None:
            st.warning("回答を選んでください。")
        else:
            st.session_state.answers.append(
                {
                    "id": q["id"],
                    "domain": q["domain"],
                    "question": q["q"],
                    "user_answer": choice,
                    "correct_answer": q["answer"],
                    "is_correct": choice == q["answer"],
                    "weight": q["weight"],
                    "expl": q["expl"],
                }
            )

            if choice == q["answer"]:
                st.session_state.raw_scores[q["domain"]] += q["weight"]

            if q_idx < total_questions - 1:
                st.session_state.current_index += 1
            else:
                st.session_state.finished = True

            st.rerun()


# =========================
# 結果画面
# =========================
else:
    st.balloons()
    st.title("🏁 測定完了")
    st.subheader("結果レポート")

    domain_max_scores = get_domain_max_scores(QUESTIONS)

    domain_indices = {}
    for domain in DOMAINS:
        domain_indices[domain] = convert_domain_score(
            st.session_state.raw_scores[domain],
            domain_max_scores[domain]
        )

    fsiq = calc_fsiq(domain_indices)
    band = get_iq_band_comment(fsiq)

    st.metric("総合推定IQ", f"{fsiq}")
    st.write(f"判定：**{band}**")

    st.write("---")
    st.subheader("4領域指数")

    for domain in DOMAINS:
        label = DOMAIN_LABELS[domain]
        raw = st.session_state.raw_scores[domain]
        raw_max = domain_max_scores[domain]
        index_score = domain_indices[domain]

        st.markdown(f"### {domain} / {label}")
        st.write(f"- 素点: **{raw} / {raw_max}**")
        st.write(f"- 領域指数: **{index_score}**")
        st.write(f"- コメント: {get_domain_comment(domain, index_score)}")

    strongest = max(domain_indices, key=domain_indices.get)
    weakest = min(domain_indices, key=domain_indices.get)

    st.write("---")
    st.subheader("認知プロフィールまとめ")
    st.write(f"- 最も高い領域: **{strongest} / {DOMAIN_LABELS[strongest]}**")
    st.write(f"- 最も低い領域: **{weakest} / {DOMAIN_LABELS[weakest]}**")

    st.write("---")
    st.subheader("答え合わせ")

    for i, ans in enumerate(st.session_state.answers, start=1):
        mark = "✅" if ans["is_correct"] else "❌"
        with st.expander(f"問{i} {mark} {ans['question'][:20]}..."):
            st.write(f"**あなたの回答:** {ans['user_answer']}")
            st.write(f"**正解:** {ans['correct_answer']}")
            st.write(f"**配点:** {ans['weight']}点")
            st.info(ans["expl"])

    st.write("---")
    if st.button("もう一度受ける"):
        st.session_state.started = False
        st.session_state.current_index = 0
        st.session_state.answers = []
        st.session_state.raw_scores = {domain: 0 for domain in DOMAINS}
        st.session_state.finished = False
        st.rerun()
