#include <stdio.h>
#include <stdlib.h>
#include "binary_trees.h"

/**
 *
 *
 *
 */

binary_tree_t *binary_tree_insert_left(binary_tree_t *parent, int value)
{
	binary_tree_t *temp = NULL;
	
	if (parent == NULL)
		return (NULL);

	temp = malloc(sizeof(binary_tree_t));
	if (temp == NULL)
		return (NULL);

	temp->n = value;
	temp->parent = parent;
	temp->left = NULL;
	temp->right = NULL;

	if (parent->left != NULL)
	{
		temp->left = parent->left;
		temp->left->parent = temp;
	}

	parent->left = temp;
	return (parent);
}
