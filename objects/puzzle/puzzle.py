class Puzzle:

    _struct = None
    _render_queue = None
    wireframe = False

    def __init__(self, root):
        self.root = root
        self.camera = self.root.root.camera
        self.pg = self.root.root.pg
        self._render_queue = []

    @staticmethod
    def puzzle_default_preset_load(presets, preset_num):
        return presets[preset_num]

    def puzzle_gen(self):
        self.puzzle_struct_init()
        self.puzzle_parts_build(self.puzzle_parts_gen())

    def puzzle_parts_build(self, struct_coordinates):
        for i in range(len(struct_coordinates)):
            for j in range(len(struct_coordinates[i])):
                self._struct[i][j][0] = struct_coordinates[i][j]

    def render_queue_init(self, cls):
        for parts in self._struct:
            for part in parts:
                for i in range(len(part[0])):
                    self._render_queue.append(
                        cls(self.root, [part[0][i], part[1]])
                    )

    def render_queue_order(self):
        depth = []
        for el in self._render_queue:
            depth.append(el.depth)
        return sorted(range(len(self._render_queue)), key=lambda i: depth[i], reverse=1)

    def render(self):
        display = self.render_queue_order()
        for i in display:
            self._render_queue[i].render()
