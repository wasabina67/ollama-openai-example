import openai


def main():
    client = openai.OpenAI(
        base_url = "http://localhost:11434/v1",
        api_key="api_key",
    )

    resp = client.chat.completions.create(
        model="gpt-oss:20b",
        messages=[
            {"role": "system", "content": "あなたは優秀なアシスタントです。"},
            {"role": "user", "content": "こんにちは。何かダジャレを言ってください。"},
        ]
    )

    print(resp.choices[0].message.content)


if __name__ == "__main__":
    main()
