# Path-Finder-Visualizer

## Algorithms

These can be found in the `algorithms.py` file. I've implemented three finding algorithms, each of which use their corresponding data structure (`data_structures.py` file):
  1. Depth-First-Search
  2. Breath-First-Search
  3. A*
  
## How to use it

The instructions for using it are very simple:

  1. Select your algorithm. To do so you have to specify the corresponding key (in the main function). 
  2. Before any wall is drawn, the program itself manages the option to begin drawing the begin node (yellow color) and the goal node (red color). You have to select those positions by clicking the nodes. First will be drawn the begin node and then the end node. If the position you have selected is not the desired one, you only need to click again over the node in order to delete it. This way you can draw it again.
  3. Once the begin node and the goal node are drawn, you can draw the walls by pressing the mouse. If you want to delete some wall all you have to do is press the **R** key. When you are done deleting walls, if you wanted to add more you would have to press the **SPACE** key. That way the option to draw more walls is again available. 
  4. To see how the algorithm works you would have to press the **S** key. 
  
 **Last comments**
 
 If you press the **M** key, a maze will be generated for you. It uses some kind of intuitive recursive algorithm, but the results are very satisfactory. 

