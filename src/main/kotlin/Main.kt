fun main(){
    val story1 = Story("The Lion and the zebra", 10, "Helping others", "Children")
    val story2 = Story("The Tortoise and the Hare", 15, "hardwork", "Children")

val storyteller = StoryTeller("Lekishon Sheila")
storyteller.addStory(story1)
storyteller.addStory(story2)
storyteller.tellStory(story1)

val translator = Translator(listOf(story1, story2), listOf("French", "Spanish"))
translator.translate(story2, "Kiswahili")
}



data class Story(val title: String, val length: Int, val moralLesson: String, val ageGroup: String)
class StoryTeller(val name: String, val stories: MutableList<Story> = mutableListOf()) {
    fun addStory(story: Story) {
        stories.add(story)
    }

    fun tellStory(story: Story) {
        println("The storyTeller $name tells the story: ${story.title}")
    }
}


class Translator(val stories: List<Story>, val languages: List<String>) {
    fun translate(story: Story, language: String) {
        if (stories.contains(story) && languages.contains(language)) {
            println("Translating story '${story.title}' into $language")
        } else {
            println("Translation for '${story.title}' or language '$language' is not available")
        }
    }
}

