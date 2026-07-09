from tools import get_full_metadata

print(
    get_full_metadata.invoke(
        {
            "url":"https://www.youtube.com/watch?v=rhioAEy5Pss&list=PLxNHpNhDaEFJBMvkFSGxFCUzbKNa6DbGu&index=6"
        }
    )
)