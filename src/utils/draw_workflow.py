def draw(workflow):
        """Draw the workflow graph using Mermaid (no pygraphviz needed)"""
        try:
            png_data = workflow.get_graph().draw_mermaid_png()
            
            with open("workflow_graph.png", "wb") as f:
                f.write(png_data)
            
            print("✅ Workflow graph saved to workflow_graph.png")
            
            try:
                from IPython.display import Image, display
                display(Image(png_data))
            except:
                pass
                
        except Exception as e:
            print("📊 Workflow Graph (Mermaid syntax):")
            print(self.workflow.get_graph().draw_mermaid())
            print("\nPaste the above into https://mermaid.live/ to visualize")