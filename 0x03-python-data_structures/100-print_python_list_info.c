#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - print python info
 * @p: PyObject
 *
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_size(p);
	int i;
	PyListObject *ob = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", ob->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(ob->ob_item[i]->tp_name);
}
