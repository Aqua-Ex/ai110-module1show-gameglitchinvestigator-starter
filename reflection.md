# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  I noticed quite a few bugs. First of all the higher, lower system is broken. I guessed 99 at one point and it told me to go higher which would mean the answer is 100 but it was not. Another bug I noticed is that I guessed 50 and got the secret number 'right' but the secret number was actually 22. I was also unable to restart the game after winning. Lastly, I was able to guess numbers outside the range and the hints did not match the position of the numbers.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion you accepted and why.
- Give one example of an AI suggestion you changed or rejected and why.

I used Copilot on this project. An example of a suggestion I accepted is the change to the parse_guess logic. I never rejected an AI solution as I found them all to be pretty accurate when I read through them, I did however change some code related to the parse_guess function because it forgot to account for added parmeters in the function definition.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

--- I used a mixture of unit test and manual testing to decide if a bug was really fixed. I noticed that the program was allowing numbers outside of the corresponding range to be allowed as attempts. After fixing this I added a unit test to check if numbers outside the range counted as valid and also did some manual testing to confirm the results. AI did design most of the test based on new code that was added, I wouldn't say it helped me understand the test.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

Streamlit reruns code each time a user clicks a button, however session state allows for variables to stay/persists across reruns. The secret number kept changing because the variable was not being persisted throughout reruns. I used a session state to persist the secret number across reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

Giving the agent more context when prompting is something I want to continue doing in order to get better results. Next time I work with AI i'll commit more frequently so that I don't lose important working code. This project helped me see how powerful AI is for coding but how it is still very flawed in many aspects.