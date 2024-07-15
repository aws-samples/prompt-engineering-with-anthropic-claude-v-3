exercise_1_1_hint = """이 연습에서 채점 기능은 정확히 아라비아 숫자 "1", "2", "3"이 포함된 답을 찾고 있습니다. Claude에게 단순히 묻는 것만으로도 원하는 대로 할 수 있습니다."""

exercise_1_2_hint = """이 연습에서 채점 기능은 "soo" 또는 "giggles"가 포함된 답을 찾고 있습니다. 이것을 해결할 수 있는 많은 방법이 있습니다. 그냥 물어보세요!"""

exercise_2_1_hint ="""이 연습에서 채점 기능은 "hola"라는 단어가 포함된 답을 찾고 있습니다. 사람과 대화할 때처럼 Claude에게 스페인어로 대답하라고 요청하세요. 그렇게 간단합니다!"""

exercise_2_2_hint = """이 연습에서 채점 기능은 정확히 "Michael Jordan"을 찾고 있습니다. 다른 사람에게 이렇게 요청하겠습니까? 다른 말 없이 그 이름만 대답하겠습니까? 이 답변에 접근할 수 있는 여러 가지 방법이 있습니다."""

exercise_2_3_hint = """이 셀의 채점 기능은 800단어 이상의 응답을 찾고 있습니다. 아직 LLM이 단어 개수를 잘 세지 못하므로, 목표치를 넘쳐야 할 수도 있습니다."""

exercise_3_1_hint = """이 연습에서 채점 기능은 "incorrect" 또는 "not correct"라는 단어가 포함된 답을 찾고 있습니다. Claude에게 수학 문제를 더 잘 풀 수 있는 역할을 주세요!"""

exercise_4_1_hint = """이 연습에서 채점 기능은 "haiku"와 "pig"라는 단어가 포함된 해답을 찾고 있습니다. 주제를 대체하고 싶은 곳에 정확한 구문 "{TOPIC}"을 포함하는 것을 잊지 마세요. "TOPIC" 변수 값을 변경하면 Claude가 다른 주제로 하이쿠를 쓰게 됩니다."""

exercise_4_2_hint = """이 연습에서 채점 기능은 "brown"이라는 단어가 포함된 응답을 찾고 있습니다. "{QUESTION}"을 XML 태그로 둘러싸면 Claude의 응답이 어떻게 변하나요?"""

exercise_4_3_hint = """이 연습에서 채점 기능은 "brown"이라는 단어가 포함된 응답을 찾고 있습니다. 가장 의미가 없어 보이는 부분부터 한 단어 또는 문자 부분을 제거해 보세요. 한 번에 한 단어씩 제거하면서 Claude가 어느 정도 구문을 해석하고 이해할 수 있는지 확인할 수 있습니다."""

exercise_5_1_hint = """이 연습의 채점 기능은 "Warrior"라는 단어가 포함된 응답을 찾고 있습니다. Claude의 어조로 더 많은 단어를 써서 Claude가 원하는 대로 행동하도록 유도하세요. 예를 들어 "Stephen Curry is the best because(Stephen Curry가 최고인 이유는)"라고 하는 대신에 "Stephen Curry is the best and here are three reasons why. 1:(Stephen Curry가 최고인 3가지 이유는 다음과 같다. 1:)"라고 할 수 있습니다."""

exercise_5_2_hint = """이 채점 기능은 5줄 이상의 길이이며 "cat"과 "<haiku>"라는 단어가 포함된 응답을 찾고 있습니다. 간단하게 시작하세요. 현재 프롬프트는 Claude에게 하이쿠 하나를 요청합니다. 이를 변경하여 둘(또는 그 이상)을 요청할 수 있습니다. 그런 다음 서식 문제가 발생하면 프롬프트를 변경하여 Claude가 이미 하이쿠를 여러 개 썼다면 수정할 수 있습니다."""

exercise_5_3_hint = """이 연습에서 채점 기능은 "tail", "cat", "<haiku>"라는 단어가 포함된 응답을 찾고 있습니다. 이 연습을 여러 단계로 나누는 것이 도움이 됩니다.
1 .초기 프롬프트 템플릿을 수정하여 Claude가 두 편의 시를 작성하도록 합니다.
2. Claude에게 시의 주제에 대한 힌트를 줍니다. 하지만 주제를 직접 적는(예: 개, 고양이 등) 대신 "{ANIMAL1}"과 "{ANIMAL2}"와 같은 키워드로 대체합니다.
3. 프롬프트를 실행하고 변수 대체가 제대로 되었는지 확인합니다. 그렇지 않다면 {중괄호} 태그의 철자와 f-string 중괄호 형식이 올바른지 확인하세요."""

exercise_6_1_hint = exercise_6_1_hint = """이 연습의 채점 기능은 올바른 범주화 문자와 닫는 괄호, 그리고 범주 이름의 첫 글자(예: "C) B" 또는 "B) B" 등)를 찾고 있습니다.
이 연습을 한 단계씩 진행해 봅시다:
1. Claude가 어떤 범주를 사용할지 알 수 있을까요? 알려주세요! 프롬프트에 직접 사용할 4개의 범주를 포함시키세요. 쉬운 분류를 위해 괄호 문자도 포함하는 것을 잊지 마세요. XML 태그를 사용하여 프롬프트를 구성하고 Claude에게 범주가 어디에서 시작하고 끝나는지 명확히 알려주셔도 좋습니다.
2. Claude가 범주화와 범주화만을 즉시 답변하도록 하려면 불필요한 텍스트를 줄이세요. 이를 위해 여러 가지 방법이 있습니다. Claude를 대신하여 말하거나(답변의 첫 부분에서부터 하나의 열린 괄호까지 제공하여 Claude가 괄호 문자를 답변의 첫 부분으로 인식하도록 합니다), Claude에게 범주화와 범주화만을 원한다고 말하고 서문은 건너뛸 수 있습니다.
3. Claude가 여전히 잘못 범주화하거나 답변에 범주 이름을 포함하지 않을 수 있습니다. 이를 수정하려면 Claude에게 답변에 전체 범주 이름을 포함하라고 지시하세요.
4. 프롬프트 템플릿에 {email}이 포함되어 있는지 확인하세요. 그래야 Claude가 평가할 이메일을 올바르게 대체할 수 있습니다."""

exercise_6_1_solution = """
USER TURN
Please classify this email into the following categories: {email}

Do not include any extra words except the category.

<categories>
(A) Pre-sale question
(B) Broken or defective item
(C) Billing question
(D) Other (please explain)
</categories>

ASSISTANT TURN
(
"""

exercise_6_2_hint = """이 연습에서 채점 기능은 <answer> 태그로 묶인 정확한 문자만을 찾습니다. 예를 들어 "<answer>B</answer>"와 같습니다. 정확한 범주화 문자는 위의 연습과 동일합니다.
가장 간단한 방법은 Claude에게 원하는 출력 형식의 예를 보여주는 것입니다. 예를 <example></example> 태그로 감싸는 것을 잊지 마세요! 또한 Claude의 응답을 미리 채우면 Claude가 실제로 그 내용을 응답의 일부로 출력하지 않습니다."""

exercise_7_1_hint = """Claude에게 예제 이메일을 작성하고 분류해야 합니다(원하는 정확한 형식으로). 이를 수행하는 방법은 여러 가지가 있습니다. 아래 지침을 참조하세요.
1. 최소 두 개의 예제 이메일을 사용해 보세요. 모든 범주에 대한 예제가 필요한 것은 아닙니다. 긴 예제일 필요도 없습니다. 6장 연습문제 1의 마지막 부분에서 생각해 본 것처럼 까다로운 범주에 대한 예제가 더 도움이 됩니다. XML 태그를 사용하면 예제를 프롬프트의 나머지 부분과 구분할 수 있지만 필수는 아닙니다.
2. 예제 답변 형식이 원하는 형식과 정확히 일치하도록 하세요. 그러면 Claude도 그 형식을 모방할 수 있습니다. 이 형식은 Claude의 답변이 범주 문자로 끝나도록 해야 합니다. {email} 자리 표시자를 어디에 배치하든 예제 이메일과 정확히 동일한 형식이어야 합니다.
3. 프롬프트 자체에 범주 목록을 포함하고 {email} 자리 표시자를 포함해야 합니다. 그렇지 않으면 Claude가 참조할 범주를 알 수 없습니다."""

exercise_7_1_solution = """
USER TURN
Please classify emails into the following categories, and do not include explanations: 
<categories>
(A) Pre-sale question
(B) Broken or defective item
(C) Billing question
(D) Other (please explain)
</categories>

Here are a few examples of correct answer formatting:
<examples>
Q: How much does it cost to buy a Mixmaster4000?
A: The correct category is: A

Q: My Mixmaster won't turn on.
A: The correct category is: B

Q: Please remove me from your mailing list.
A: The correct category is: D
</examples>

Here is the email for you to categorize: {email}

ASSISTANT TURN
The correct category is:
"""
exercise_8_1_hint = """이 연습 문제의 채점 기능은 "I do not", "I don't", "Unfortunately"라는 문구가 포함된 응답을 찾고 있습니다. Claude가 답을 모르는 경우 어떻게 해야 합니까?"""

exercise_8_2_hint = """이 연습 문제의 채점 기능은 "49-fold"라는 문구가 포함된 응답을 찾고 있습니다. Claude가 작업과 사고 과정을 보여주도록 하십시오. 먼저 관련 인용구를 추출하고 인용구가 충분한 증거를 제공하는지 확인하십시오. 8장 수업 내용을 다시 보고 싶다면 참조하십시오."""

exercise_9_1_solution = """
You are a master tax acountant. Your task is to answer user questions using any provided reference documentation.

Here is the material you should use to answer the user's question:
<docs>
{TAX_CODE}
</docs>

Here is an example of how to respond:
<example>
<question>
What defines a "qualified" employee?
</question>
<answer>
<quotes>For purposes of this subsection—
(A)In general
The term "qualified employee" means any individual who—
(i)is not an excluded employee, and
(ii)agrees in the election made under this subsection to meet such requirements as are determined by the Secretary to be necessary to ensure that the withholding requirements of the corporation under chapter 24 with respect to the qualified stock are met.</quotes>

<answer>According to the provided documentation, a "qualified employee" is defined as an individual who:

1. Is not an "excluded employee" as defined in the documentation.
2. Agrees to meet the requirements determined by the Secretary to ensure the corporation's withholding requirements under Chapter 24 are met with respect to the qualified stock.</answer>
</example>

First, gather quotes in <quotes></quotes> tags that are relevant to answering the user's question. If there are no quotes, write "no relevant quotes found".

Then insert two paragraph breaks before answering the user question within <answer></answer> tags. Only answer the user's question if you are confident that the quotes in <quotes></quotes> tags support your answer. If not, tell the user that you unfortunately do not have enough information to answer the user's question.

Here is the user question: {QUESTION}
"""

exercise_9_2_solution = """
You are Codebot, a helpful AI assistant who finds issues with code and suggests possible improvements.

Act as a Socratic tutor who helps the user learn.

You will be given some code from a user. Please do the following:
1. Identify any issues in the code. Put each issue inside separate <issues> tags.
2. Invite the user to write a revised version of the code to fix the issue.

Here's an example:

<example>
<code>
def calculate_circle_area(radius):
    return (3.14 * radius) ** 2
</code>
<issues>
<issue>
3.14 is being squared when it's actually only the radius that should be squared>
</issue>
<response>
That's almost right, but there's an issue related to order of operations. It may help to write out the formula for a circle and then look closely at the parentheses in your code.
</response>
</example>

Here is the code you are to analyze:

<code>
{CODE}
</code>

Find the relevant issues and write the Socratic tutor-style response. Do not give the user too much help! Instead, just give them guidance so they can find the correct solution themselves.

Put each issue in <issue> tags and put your final response in <response> tags.
"""

exercise_10_2_1_toolspec = """
toolConfig = {
  "tools": [
    {
      "toolSpec": {
        "name": "generate_wikipedia_reading_list",
        "description": "A tool is used to search Wikipedia for details related to the topic provided by the user.",
        "inputSchema": {
          "json": {
            "type": "object",
            "properties": {
              "research_topic": {
                "type": "string",
                "description": "The topic to search for on wikipedia."
              },
              "article_titles": {
                "type": "string",
                "description": "a list of strings, where each string represents a potential wikipedia article title to research"
              }
            },
            "required": ["research_topic", "article_titles"]
          }
        }
      }
    }
  ]
}
"""

exercise_10_2_1_code = """
def get_research_help(research_topic, num_articles=3):
    system_prompt = "You are a helpful AI research assistant. You have access to the get_research_help tool that will be used to search Wikipedia for deatils related to the topic provided by the user."

    prompt = f"I need help gathering research on the {research_topic}, to assist me I need you to creat {num_articles} article(s) related Wikipedia article titles on the topic."

    messages = [{"role": "user", "content": [{"text": prompt}]}]

    converse_api_params = {
        "modelId": modelId,
        "system": [{"text": system_prompt}],
        "messages": messages,
        "inferenceConfig": {"temperature": 0.0, "maxTokens": 2000},
        "toolConfig": toolConfig,
    }

    response = bedrock_client.converse(**converse_api_params)

    if response['stopReason'] == "tool_use":
        tool_use = response['output']['message']['content'][-1]
        tool_name = tool_use['toolUse']['name']
        tool_inputs = tool_use['toolUse']['input']

    if tool_name == "generate_wikipedia_reading_list":
        print(f"Claude wants to use the {tool_name} tool")
        research_topic = tool_inputs["research_topic"]
        articles = tool_inputs["article_titles"]
        article_titles = json.loads(articles)
        try:
            print(article_titles)
            print(f"Claude is now calling the {tool_name} to research {research_topic}")
            generate_wikipedia_reading_list(research_topic, article_titles)
        except ValueError as e:
            print(f"Error: {str(e)}")

"""

exercise_10_2_2_toolSpec = """
toolConfig = {
  "tools": [
    {
      "toolSpec": {
        "name": "translations_from_claude",
        "description": "The translations from Claude of a user provided phrase into English to Spanish, French, Japanese, and Arabic.",
        "inputSchema": {
          "json": {
            "type": "object",
            "properties": {
              "english": {"type": "string", "description": "Your English translation of the provided content from the user"},
              "spanish": {"type": "string", "description": "Your Spanish translation of the provided content from the user"},
              "french": {"type": "string", "description": "Your French translation of the provided content from the user"},
              "japanese": {"type": "string", "description": "Your Japanese translation of the provided content from the user"},
              "arabic": {"type": "string", "description": "Your Arabic translation of the provided content from the user"}
            },
            "required": ["english", "spanish", "french", "japanese", "arabic"]
          }
        }
      }
    }
  ],
    "toolChoice": {"tool": {"name": "translations_from_claude"}}
}
"""

exercise_10_2_2_translate = """
def translate(query):
    prompt = f"Translate this phrase from the user into English, Spanish, French, Japanese and Arabic. Content to translate: '{query}'"

    converse_api_params = {
        "modelId": modelId,
        "messages": [{"role": "user", "content": [{"text": prompt}]}],
        "additionalModelRequestFields": {"max_tokens": 4096},
        "toolConfig": toolConfig
    }

    response = bedrock_client.converse(**converse_api_params)
    tool_use = response['output']['message']['content'][-1]
    translations_from_claude = tool_use['toolUse']['input']

    print(json.dumps(translations_from_claude, ensure_ascii=False, indent=2))
"""