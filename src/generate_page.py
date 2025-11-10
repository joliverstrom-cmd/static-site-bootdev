from block_to_html import markdown_to_htmlnode
import os

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line[:2] == "# ":
            return line[2:].strip()
        
    raise Exception("No h1 title available")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        markdown = f.read()

    with open(template_path) as t:
        template = t.read()

    html_node = markdown_to_htmlnode(markdown)
    content = html_node.to_html()
    title = extract_title(markdown)

    display = template.replace("{{ Title }}",title).replace("{{ Content }}", content)
    display = display.replace('href="/',f'href="{basepath}').replace('src="/',f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path),exist_ok=True)

    with open(dest_path, "w") as dest:
        dest.write(display)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    paths = os.listdir(dir_path_content)
    for path in paths:
        file_origin = os.path.join(dir_path_content,"index.md")
        path_origin = os.path.join(dir_path_content,path)
        path_dest = os.path.join(dest_dir_path, path)
        file_dest = os.path.join(dest_dir_path, "index.html")
        if os.path.isdir(path_origin):
            generate_pages_recursive(path_origin, template_path, path_dest, basepath)
        else:
            generate_page(file_origin,template_path,file_dest, basepath)
        
    

    