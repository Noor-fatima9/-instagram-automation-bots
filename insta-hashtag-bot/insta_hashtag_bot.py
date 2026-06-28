import requests
from bs4 import BeautifulSoup

HASHTAG_DB = {
    "fashion": ["#fashion", "#style", "#ootd", "#fashionista", "#lookbook", "#instafashion", "#fashionblogger", "#styleinspo", "#outfitinspo", "#fashiondaily"],
    "fitness": ["#fitness", "#gym", "#workout", "#fit", "#fitnessmotivation", "#gymlife", "#fitnessjourney", "#gymmotivation", "#fitspo", "#healthylifestyle"],
    "food": ["#food", "#foodie", "#instafood", "#foodporn", "#yummy", "#foodphotography", "#delicious", "#foodlover", "#homecooking", "#tasty"],
    "travel": ["#travel", "#wanderlust", "#travelgram", "#instatravel", "#adventure", "#explore", "#vacation", "#travelphotography", "#trip", "#nature"],
    "business": ["#business", "#entrepreneur", "#motivation", "#success", "#marketing", "#entrepreneurlife", "#smallbusiness", "#startup", "#businessowner", "#grind"],
    "beauty": ["#beauty", "#makeup", "#skincare", "#beautyblogger", "#makeuplover", "#cosmetics", "#glowingskin", "#beautycommunity", "#makeupartist", "#selfcare"]
}

def generate_hashtags(niche, count=30):
    niche = niche.lower().strip()
    base_tags = HASHTAG_DB.get(niche, HASHTAG_DB["business"])
    all_tags = base_tags.copy()
    mid_tags = [f"#{niche}love", f"#{niche}community", f"#{niche}life", f"daily{niche}", f"{niche}inspo"]
    small_tags = [f"#{niche}usa", f"#{niche}girl", f"#{niche}style2026", f"trending{niche}"]
    all_tags.extend(mid_tags)
    all_tags.extend(small_tags)
    unique_tags = list(dict.fromkeys(all_tags))[:count]
    return unique_tags
def main():
    print("="*50)
    print(" INSTAGRAM HASHTAG GENERATOR BOT ")
    print("="*50)
    
    niche = input("\nEnter your Niche [fashion, fitness, food, travel, business, beauty]: ")
    count = input("How many hashtags do you want? [Default 30]: ")
    
    try:
        count = int(count) if count else 30
    except:
        count = 30
    
    hashtags = generate_hashtags(niche, count)
    
    print("\n✅ HERE ARE YOUR VIRAL HASHTAGS:")
    print("-"*50)
    print(" ".join(hashtags))
    print("-"*50)
    print(f"\nTotal: {len(hashtags)} hashtags")
    print("Tip: Use all 30 hashtags. First 5 are the strongest.")
    
    # Save to TXT file
    filename = f"{niche}_hashtags.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(" ".join(hashtags))
    print(f"Saved to: {filename}")

if __name__ == "__main__":
    main()