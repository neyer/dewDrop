# dewDrop : an attestation network


# what

dewDrop is a network where nodes make statements about other nodes. those statements can be transitively followed so individual nodes can make queries which aggregate information over the network.

there are two parts
 - a server which acccepts statements and returns queries about statements. there's an iplementation running at:
  https://dewdrop.neyer.me

- a chrome extension which you can use to trust users on facebook. there's work being done on the UI in a seprate branch

# how

 at the core is trust. nodes can issue statements that say 'node X trusts node Y'. right now that's all there is to it - a server that accepts statements frorm users and can tell you which statements you've made, and which statements other users have made about a user.



# how we want to extend it

   - there's no authentication. the server accepts statements from any id
     we need the server to associate id's with accounts, so that a user has to
     verify that they own an id before making statements on its behalf.

   - there's no transitive following of links. right now you can just see which identities trust other identities. there's no way to transitively see if there are trust paths from you to another node.

   - update the chrome extension with a better ui and support for more networks

   - add extensions for twitter, reddit, hacker news

   - move the server somewhere better

   - (future?) use a blockchain to store trust statments 


please help!


license:

bsd
