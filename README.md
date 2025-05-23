# RecSys2025

Work for the course Multimodal Recommendation Systems and Complex Networks.  
This repository contains a small part of the SimSom simulator, under development for [CARISMA project](carisma-project.org).  
The simulator consists of a simulation of a social platform where users interact with each other through messages.

## Table of Contents
- [Description](#description)
- [Objective](#objective)
- [Usage](#usage)

## Description
The code represents a small part of the actual simulator, where the key elements are users and messages. 
The following section will briefly describe the main classes and how they work.

### `user.py`

- This module defines the **`User`** class, representing a user in a social network simulation.
- The user can perform actions (such as posting something or re-sharing something).
- This class will not need to be modified; the description is to provide information about its role.

### Key Features

- **Topics**  
  Each user has a vector to represent their interests, this vector contains values from 0 to 1 depending on how much a given topic interests them the most:  
  ```python
  self.interests = [0.2, 0.8, 0.5]  # Example: values between 0 and 1
  ```
- **Followers and followings**  
  Each user has a list of followers and following.
- **Feed**  
  Each user has a newsfeed (or feed) that contains a series of posts, this list is basically what the user sees when they open the social's homepage. 

---

### `action.py`

- This module defines the **`Action`** class, representing a generic action in the simulator.
- This class is not relevant, this is a parent class used for the development of the **`View`** and **`Message`** classes.
- This class will not need to be modified; the description is to provide information about its role.

---

### `view.py`

- This module defines the **`View`** class, representing the action of view a message inside the feed when the user perform a reshare.
- This class is not relevant for the project.
- This class will not need to be modified; the description is to provide information about its role.

---

### `message.py`

- This module defines the **`Message`** class, representing a message object that can be a post or repost.
- You can take advantage of the combination of class properties to sort the content to recommend.
- This class will not need to be modified; the description is to provide information about its role.

### Key Features

- **Quality**  
  Each message has a quality that indicates how good the message content is. The value of this field depends on a value obtained from a custom beta distribution, each user has the same distribution. Keep this value in mind because people generally tend to give more weight to messages with good quality than messages with low quality. Its value is between 0 and 1.
- **Topics**  
  Similarly to users, each message has a list of topics. This list is assigned to it within the **`User`** class, via a sampling mechanism. Keep this list in mind since there is a tendency to suggest content that may be of interest to users rather than content that has topics that target users are not interested in. 
- **Appeal**  
  Each message has an appeal that indicates how interesting the message content is. The value of this field is obtained by a right-skewed distribution via inverse transform sampling. Keep this value in mind because people generally tend to give more weight to messages with high appeal than messages with low appeal. Its value is between 0 and 1.

---

### `main.py`

- This module defines the **`Main`** class, it's the class where you actually have to implement code.

### Target classes

- **DataManager**  
  This class basically deals with managing data flows to the recommendation mechanism. 
  What happens in a nutshell is that a network of users is created by exploiting a function, and each user is in charge of performing one or more actions (making posts or re-shares) that are assigned an incremental time T.
  ```python
    for agent in self.agents.values():
              actions, _ = agent.make_actions()
              for action in actions:
                  action.time = self.clock.next_time()   
  ```
  You will have to dunquere write the code that takes care of sending the data to perform the recommendation mechanism in the `send_recsys` function.
  ```python
   def send_recsys(self, user: User) -> tuple:
        # Implement the logic to send messages to RecSys
        return None, None # Placeholder for messages
  ```
- **RecSys**  
  This class is in charge of making the recommendation for users, thus going to build the feed for each user. 
  Through the `build_feed` function you will have to create a list of messages per user, which will then become his feed.
  ```python
    def build_feed(self, agent: User, X, Y) -> list: # Placeholder for messages
        # Build a newsfeed for the agent based on incoming and outgoing messages
        # agent.newsfeed = generated_feed
        return [] # return the genereated_feed
  ```

## Objective
The goal of the project is to implement a recommender system that can have, within each user's homepage a series of posts sorted according to a chosen logic (e.g. you can leverage topic vectors to recommend content that has similar topics to the user's interests, you can recommend posts from friends and non-proprotectionally, etc).
You will have to work in the `main.py` class, without modifying the other classes, which you can still analyze to better understand how the code works.
The output should be a file that contains, for each user, their feed after recommendation.

## Usage
1. Clone the repository:
```bash
 git clone https://github.com/gi-ux/RecSys2025.git
```

2. Create a new env (example with conda)
 ```bash
 conda create --name work_env python==3.10
```

3. Install dependencies:
```bash
 pip install -r requirements.txt
 ```

