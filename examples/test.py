from html2text import HTML2Text

raw_html = """
<p>hi</p>
<ol>
    <li>Integration with Github</li>
    <li>
        <p>Integration with Freshdesk</p>
        <ol>
            <li>
                <p>Create the freshdesk app on the app store for internal use.</p>
                <p>Requirement: 1. Build it as an "external app" 2. User should find the app on the app store 3. It should have the meta data needed to host an app on the marketplace: a. Overview b. Installation instructions c. Privacy &amp; Security policy 4. The Knowledge Keeper app will be a serveless app. Freshdesk documentation. 5. We need to define the app manifest and setup events. see above documentation 6. Define environment variables. see this doc 7. Define the installation parameters. See this doc 8. Then submit the app to freshdesk by following this documentation</p>
            </li>
            <li>
                <p>Connect knowldge keeper to freshdesk.</p>
            </li>
            <li>
                <p>Implement the following flow:</p>
                <ol>
                    <li><p>Support agent action to forward ticket as byte.</p>
                        <ol>
                            <li>first item</li>
                            <li>second item</li>
                        </ol>
                    </li>
                    <li>Consume freshdesk byte and make ai edits.</li>
                    <li>Sync freshdesk knowledge base.</li>
                    <li>Productionize freshdesk implementation.</li>
                </ol>
            </li>
            <li>Support agent action to forward ticket as byte.</li>
            <li>Consume freshdesk byte and make ai edits.</li>
            <li>Sync freshdesk knowledge base.</li>
            <li>Productionize freshdesk implementation.</li>
        </ol>
    </li>
</ol>
"""
h2t = HTML2Text()
h2t.images_as_html = True
h2t.bypass_tables = True
h2t.mark_code = True
h2t.bypass_emphasis = True

print(h2t.handle(raw_html))