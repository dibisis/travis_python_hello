def test_get_helloworld():
	assert 'hello world' == get_helloworld()
def get_helloworld():
	return 'hello world'

def main():
	print(get_helloworld())
#main
if __name__=='__main__':
	main()
