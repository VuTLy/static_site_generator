_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(p