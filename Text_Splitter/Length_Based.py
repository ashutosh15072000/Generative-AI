from langchain.text_splitter import CharacterTextSplitter

text="""
More than fifty years of human activity in space have produced societal benefits that improve
the quality of life on Earth. The first satellites, designed to study the space environment and
test initial capabilities in Earth orbit, contributed critical knowledge and capabilities for
developing satellite telecommunications, global positioning, and advances in weather
forecasting. Space exploration initiated the economic development of space that today, year
after year, delivers high returns for invested funds in space1
. The challenges of space
exploration have sparked new scientific and technological knowledge of inherent value to
humankind, leading to better understanding of our Universe and the solar system in which we
live. Knowledge, coupled with ingenuity, provides people around the globe with solutions as
well as useful products and services. Knowledge acquired from space exploration has also
introduced new perspectives on our individual and collective place in the Universe.  
Future space exploration goals call for sending humans and robots beyond Low Earth Orbit and
establishing sustained access to destinations such as the Moon, asteroids and Mars. Space
agencies participating in the International Space Exploration Coordination Group (ISECG)2 are
discussing an international approach for achieving these goals, documented in ISECG's Global
Exploration Roadmap3
. That approach begins with the International Space Station (ISS), and
leads to human missions to the surface of Mars.  
Employing the complementary capabilities of both humans and robotic systems will enable
humankind to meet this most ambitious space exploration challenge, and to increase benefits
for society. These benefits can be categorized into three fundamental areas: innovation; culture
and inspiration; and new means to address global challenges.
Innovation. There are numerous cases of societal benefits linked to new knowledge and
technology from space exploration. Space exploration has contributed to many diverse aspects
of everyday life, from solar panels to implantable heart monitors, from cancer therapy to light‐
weight materials, and from water‐purification systems to improved computing systems and to a
global search‐and‐rescue system4
. Achieving the ambitious future exploration goals as outlined
above will further expand the economic relevance of space. Space exploration will continue to
be an essential driver for opening up new domains in science and technology, triggering other
sectors to partner with the space sector for joint research and development. This will return
immediate benefits back to Earth in areas such as materials, power generation and energy

"""

splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=""
)
text_splitter = splitter.split_text(text)

print(text_splitter)
