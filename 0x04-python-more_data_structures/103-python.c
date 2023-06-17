#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints info about Python lists.
 * @p: A list object.
 */
void print_python_list(PyObject *p)
{
	int size, alc, x;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alc);

	for (x = 0; x < size; x++)
	{
		type = list->ob_item[x]->ob_type->tp_name;
		printf("Element %d: %s\n", x, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[x]);
	}
}

/**
 * print_python_bytes - Prints info about Python byte objects.
 * @p: byte object.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char x, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);
	for (x = 0; x < size; x++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (x == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
