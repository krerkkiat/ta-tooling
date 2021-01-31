// Select the ul element containing the list of submision.

interface Entry {
    name: string;
    url: string;
}

async function postData(url: string = "", data: object = {}) {
    const response = await fetch(url, {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        headers: {
            "Content-Type": "application/json",
        },
        redirect: "manual",
        referrerPolicy: "no-referrer",
        body: JSON.stringify(data),
    });
    return response.json();
}

let target_ul: HTMLElement | null = document.querySelector("#pageList");
if (target_ul !== null) {
    let submission_list: HTMLCollection = target_ul.children || new HTMLCollection();
    let results: Entry[] = new Array<Entry>();

    for (let i = 0; i < submission_list.length; i++) {
        let entry: Entry;
        let name: string;
        let url: string;

        let name_element: HTMLElement = submission_list.item(i)?.querySelector("div.item h3") || new HTMLElement();
        let file_element: HTMLElement | null | undefined = submission_list?.item(i)?.querySelector("div.details td#meta_value_2 a");

        name = name_element.textContent || "";
        if (file_element !== null && file_element !== undefined) {
            url = (<HTMLLinkElement>file_element).href || "";
        } else {
            url = "";
        }
        results.push({ name: name, url: url });
    }

    postData("http://localhost:5000/", { submission_files: results });
}
