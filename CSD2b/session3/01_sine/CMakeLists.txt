
cmake_minimum_required(VERSION 3.29)

project(SineGenerator VERSION 0.0.1)
juce_add_console_app(SineGenerator PRODUCT_NAME "SineGenerator")
target_sources(SineGenerator PRIVATE main.cpp)
target_compile_definitions(SineGenerator PRIVATE JUCE_WEB_BROWSER=0 JUCE_USE_CURL=0)

target_link_libraries(SineGenerator
        PRIVATE
        juce::juce_audio_basics
        juce::juce_audio_devices
        juce::juce_audio_formats
        juce::juce_audio_processors

        PUBLIC
        juce::juce_recommended_config_flags
        juce::juce_recommended_warning_flags
)

target_compile_features(SineGenerator PRIVATE cxx_std_20)
