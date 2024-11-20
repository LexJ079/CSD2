
CXX = g++
CXXFLAGS = -Wall -std=c++17
TARGET = main
SRCS = main.cpp Instrument.cpp
OBJS = $(SRCS:.cpp=.o)


all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $<


clean:
	rm -f $(OBJS) $(TARGET)
