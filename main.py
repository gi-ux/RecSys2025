import igraph as ig
import random
from user import User
import os

if os.path.exists("feed.txt"):
    os.remove("feed.txt")


def init_network(net_size=2_00, p=0.5, k_out=10) -> dict:
    """
    Create a network using a directed variant of the random-walk growth model
    https://journals.aps.org/pre/abstract/10.1103/PhysRevE.67.056104
    Inputs:
        - net_size (int): number of nodes in the desired network
        - k_out (int): average no. friends for each new node
        - p (float): probability for a new node to follow friends of a
        friend (models network clustering)
    """
    if net_size <= k_out + 1: 
        return ig.Graph.Full(net_size, directed=True)

    graph = ig.Graph.Full(k_out, directed=True)
    for n in range(k_out, net_size):
        target = random.choice(graph.vs)
        friends = [target]
        n_random_friends = 0
        for _ in range(k_out - 1):
            if random.random() < p:
                n_random_friends += 1

        friends += random.sample(
            graph.successors(target), n_random_friends
        )
        friends += random.sample(range(graph.vcount()), k_out - 1 - n_random_friends)
        graph.add_vertex(name=str(n))
        edges = [(n, f) for f in friends]
        graph.add_edges(edges)
    for v in graph.vs:
        v["uid"] = f"u{v.index}"
        v["utype"] = "normal user"
        v["postperday"] = 0 if v["utype"] == "lurker" else random.uniform(0, 50)
        v["qualitydistr"] = "(0.5, 0.15, 0, 1)"
        graph.write_gml("network.gml")
    users = {}
    for node in graph.vs:
        friends = graph.successors(node.index)
        followers = graph.predecessors(node.index)
        user_i = User(
            uid=graph.vs[node.index]["uid"],
            user_class=graph.vs[node.index]["utype"],
            post_per_day=int(graph.vs[node.index]["postperday"]),
            quality_params=eval(graph.vs[node.index]["qualitydistr"]),
            friends=["u" + str(u) for u in friends],
            followers=["u" + str(u) for u in followers],
        )
        users[user_i.uid] = user_i
    return users


class ClockManager:
    """
    Class responsible for clock simulation,
    the class has the task of giving a value obtained from a distribution.
    """

    def __init__(self) -> None:
        self.current_time = 0

    def next_time(self) -> float:
        """
        Return the current time and generate the next
        Returns:
            float: current time
        """
        current = self.current_time
        self.current_time += random.random() * 0.02
        return current


class DataManager:
    def __init__(self):
        self.agents = init_network()
        self.outgoing_msgs = {uid: [] for uid in self.agents.keys()}
        self.clock = ClockManager()

    def recv_from_agents(self) -> None:
        for agent in self.agents.values():
            actions, _ = agent.make_actions()
            for action in actions:
                action.time = self.clock.next_time()   
            self.outgoing_msgs[agent.uid].extend(actions)

    def send_recsys(self, user: User) -> tuple:
        # Implement the logic to send messages to RecSys
        return X, Y # Placeholder for messages


class RecSys:
    def __init__(self):
        self.feeds = {}

    def build_feed(self, agent: User, X, Y): # Placeholder for messages
        # Build a newsfeed for the agent based on incoming and outgoing messages 


if __name__ == "__main__":

    dm = DataManager()
    rs = RecSys()

    dm.recv_from_agents()
    for agent in dm.agents.values():
        print("Processing agent: ", agent)
        X, Y = dm.send_recsys(agent)
        rs.build_feed(agent, X, Y)
        with open(f"feed.txt", "a", encoding="utf-8") as f:
            f.write(f"User Info:\n{agent}\n")
            f.write("Detailed feed:\n")
            for item in agent.newsfeed:
                f.write(f"{item}\n")
                f.write("\n")
            f.write("---------------------------------------\n")