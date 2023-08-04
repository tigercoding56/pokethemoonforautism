import pygame
import heapq

class Node:
    """
    A node class for A* Pathfinding
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0 # g = actual cost of reaching this node
        self.h = 0 # h = heuristic, used for determining which node to visit next
        self.f = 0 # f = g + h

    def __eq__(self, other):
        return self.position == other.position

    # defining less than for purposes of heap queue
    def __lt__(self, other):
        return self.f < other.f

    # defining greater than for purposes of heap queue
    def __gt__(self, other):
        return self.f > other.f


class Pathfinding:
    """
    A class for pathfinding across an image
    """

    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.start_pos = (self.width // 2, self.height // 2)
        self.target_pos = None
        self.grid = [[0 for _ in range(self.height)] for _ in range(self.width)] # initialize grid with zeros
        self.init_grid()
        self.path = []

    def init_grid(self):
        """
        Converts the image pixels to a grid of integers representing the cost of traversing each node
        """
        for x in range(self.width):
            for y in range(self.height):
                t= self.image.get_at((x,y))
                if  t == (0,0,0): # black pixel
                    self.grid[x][y] = 100 # set a high cost for traversing black nodes
                else:
                    self.grid[x][y] = int(0.1*(255-t[1]))

    def find_a_star_path(self):
        """
        Finds the shortest path from the start position to the target position using the A* algorithm
        """
        start_node = Node(None, self.start_pos)
        start_node.g = start_node.h = start_node.f = 0.0

        open_list = [start_node]
        closed_set = set()

        while len(open_list) > 0:
            current_node = heapq.heappop(open_list)

            if current_node.position in closed_set:
                continue
            closed_set.add(current_node.position)

            if current_node.position == self.target_pos:
                while current_node is not None:
                    self.path.append(current_node.position)
                    current_node = current_node.parent
                self.path.reverse()
                return

            for child_pos in self.get_neighbors(current_node.position):
                child_node = Node(current_node, child_pos)
                if child_node.position in closed_set:
                    continue

                # calculate the cost of reaching the child node
                child_node.g = current_node.g + self.grid[child_pos[0]][child_pos[1]]
                child_node.h = self.heuristic(child_pos, self.target_pos)
                child_node.f = child_node.g + child_node.h

                add_to_open = child_node.position not in [n.position for n in open_list]

                if add_to_open:
                    heapq.heappush(open_list, child_node)
                else:
                    for open_node in open_list:
                        if open_node.position == child_node.position and open_node.f > child_node.f:
                            open_node.g = child_node.g
                            open_node.h = child_node.h
                            open_node.f = child_node.f
                            open_node.parent = child_node.parent

    def get_neighbors(self, position):
        """
        Returns a list of the positions of all neighboring nodes that can be traversed
        """
        neighbors = []
        x, y = position
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if 0 <= x+dx < self.width and 0 <= y+dy < self.height:
                    if self.grid[x+dx][y+dy] < 1000000: # only add nodes that can be traversed
                        neighbors.append((x+dx, y+dy))
        return neighbors

    def heuristic(self, a, b):
        """
        Returns the Manhattan distance between two positions
        """
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def handle_events(self):
        """
        Handles Pygame events
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.target_pos = pygame.mouse.get_pos()
                    self.path = []
                    self.find_a_star_path()

    def draw(self, screen):
        """
        Draws the image and the path on the Pygame screen
        """
        screen.blit(self.image, (0, 0))

        # draw the path
        if len(self.path) > 1:
            pygame.draw.lines(screen, (255, 0, 0), False, self.path, 5)

        # draw the start and target positions
        pygame.draw.circle(screen, (0, 255, 0), self.start_pos, 10)
        if self.target_pos is not None:
            pygame.draw.circle(screen, (255, 0, 0), self.target_pos, 10)

    def run(self):
        """
        Runs the Pygame event loop
        """
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pathfinding")
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            self.handle_events()

            screen.fill((255, 255, 255))

            self.draw(screen)

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    pathfinding = Pathfinding("img/fei.png")
    pathfinding.run()