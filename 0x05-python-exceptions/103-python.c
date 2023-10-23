#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints info about Python lists
 * @p: Python object pointer
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t len, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	len = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", len);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < len; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		if (PyFloat_Check(item))
			print_python_float(item);
	}
}

/**
 * print_python_bytes - Prints info about Python bytes
 * @p: Python object pointer
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t len, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	len = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  size: %zd\n", len);
	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);

	if (len > 10)
		len = 10;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  first %zd bytes: ", len);
	for (i = 0; i < len; i++)
		printf("%02x%c", str[i] & 0xFF, (i == len - 1) ? '\n' : ' ');
}

/**
 * print_python_float - Prints info about Python float
 * @p: Python object pointer
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
