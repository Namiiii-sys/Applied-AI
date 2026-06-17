from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# schema for data format

class Reviews(BaseModel):
    key_themes: list[str] = Field(descripton="Write down all the key themes discussed in the reviews")
    Pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside the List")
    Cons: Optional[list[str]] = Field(default=None, description="Write down all the Cons inside the List")
    summary: str = Field(description="A breif summary of the review")
    sentiment: Literal["pos","neg"] = Field(description="Return sentiment be it positive negative or neutral")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")

structured_model = model.with_structured_output(Reviews)

result = structured_model.invoke("""
After using this phone for several weeks, I found it to be a well-balanced device that excels in some areas while leaving room for improvement in others. The 120Hz AMOLED display is vibrant, color-accurate, and exceptionally smooth, making content consumption and gaming enjoyable, although the automatic brightness adjustment occasionally reacts slower than expected in outdoor conditions. Performance is one of its strongest aspects, with the flagship processor delivering excellent multitasking capabilities, low application launch times, and stable frame rates in demanding games, but prolonged gaming sessions can introduce noticeable thermal buildup and minor performance throttling. The camera system captures detailed photos with strong dynamic range and pleasing color science in daylight; however, low-light shots sometimes exhibit luminance noise, oversharpening, and inconsistent white-balance behavior. Battery life comfortably lasts a full day for most users, and the fast-charging technology is genuinely convenient, though battery drain becomes more apparent when using high refresh rates, location services, and 5G connectivity simultaneously. The premium build quality, IP-rated durability, and polished software experience contribute positively to the overall user experience, yet the device attracts fingerprints easily and includes a few pre-installed applications that many users may never use. Connectivity performance is reliable thanks to modern wireless standards and strong signal retention, but the lack of expandable storage could be limiting for content creators and heavy media consumers. Overall, the smartphone successfully combines flagship-level display quality, strong computational performance, capable cameras, and dependable battery endurance, although factors such as thermal efficiency, storage limitations, premium pricing, and occasional camera inconsistencies prevent it from being a completely flawless package.

""")

print("PROS ARE: ",result.Pros)
print("\nCONS ARE: ",result.Cons)
